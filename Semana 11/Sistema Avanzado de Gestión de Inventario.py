import json
import os
from typing import Dict, List, Optional


class Producto:
    """Clase que representa un producto en el inventario"""

    def __init__(self, id: int, nombre: str, cantidad: int, precio: float):
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Métodos getter
    def get_id(self) -> int:
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def get_cantidad(self) -> int:
        return self._cantidad

    def get_precio(self) -> float:
        return self._precio

    # Métodos setter
    def set_nombre(self, nombre: str) -> None:
        self._nombre = nombre

    def set_cantidad(self, cantidad: int) -> None:
        self._cantidad = cantidad

    def set_precio(self, precio: float) -> None:
        self._precio = precio

    def to_dict(self) -> Dict:
        """Convierte el producto a diccionario para serialización"""
        return {
            'id': self._id,
            'nombre': self._nombre,
            'cantidad': self._cantidad,
            'precio': self._precio
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Producto':
        """Crea un producto desde un diccionario"""
        return cls(data['id'], data['nombre'], data['cantidad'], data['precio'])

    def __str__(self) -> str:
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"


class Inventario:
    """Clase que gestiona el inventario de productos utilizando un diccionario"""

    def __init__(self):
        # Usamos un diccionario para almacenamiento eficiente por ID
        self._productos: Dict[int, Producto] = {}
        # Usamos un conjunto para búsquedas rápidas de nombres (opcional)
        self._nombres_productos = set()

    def añadir_producto(self, producto: Producto) -> bool:
        """Añade un nuevo producto al inventario"""
        if producto.get_id() in self._productos:
            return False  # ID ya existe

        self._productos[producto.get_id()] = producto
        self._nombres_productos.add(producto.get_nombre().lower())
        return True

    def eliminar_producto(self, id: int) -> bool:
        """Elimina un producto por ID"""
        if id in self._productos:
            producto_eliminado = self._productos.pop(id)
            self._nombres_productos.discard(producto_eliminado.get_nombre().lower())
            return True
        return False

    def actualizar_producto(self, id: int, cantidad: Optional[int] = None,
                            precio: Optional[float] = None) -> bool:
        """Actualiza la cantidad y/o precio de un producto"""
        if id not in self._productos:
            return False

        producto = self._productos[id]
        if cantidad is not None:
            producto.set_cantidad(cantidad)
        if precio is not None:
            producto.set_precio(precio)

        return True

    def buscar_por_nombre(self, nombre: str) -> List[Producto]:
        """Busca productos por nombre (búsqueda parcial case-insensitive)"""
        nombre_lower = nombre.lower()
        resultados = []

        for producto in self._productos.values():
            if nombre_lower in producto.get_nombre().lower():
                resultados.append(producto)

        return resultados

    def mostrar_todos(self) -> List[Producto]:
        """Devuelve todos los productos del inventario"""
        return list(self._productos.values())

    def obtener_producto_por_id(self, id: int) -> Optional[Producto]:
        """Obtiene un producto por su ID"""
        return self._productos.get(id)

    def guardar_a_archivo(self, nombre_archivo: str = "inventario.json") -> bool:
        """Guarda el inventario en un archivo JSON"""
        try:
            datos = [producto.to_dict() for producto in self._productos.values()]
            with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")
            return False

    def cargar_desde_archivo(self, nombre_archivo: str = "inventario.json") -> bool:
        """Carga el inventario desde un archivo JSON"""
        try:
            if not os.path.exists(nombre_archivo):
                return False

            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)

            # Limpiar el inventario actual
            self._productos.clear()
            self._nombres_productos.clear()

            # Cargar nuevos productos
            for producto_data in datos:
                producto = Producto.from_dict(producto_data)
                self.añadir_producto(producto)

            return True
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")
            return False


class SistemaInventario:
    """Clase principal que maneja la interfaz de usuario y la lógica del sistema"""

    def __init__(self):
        self.inventario = Inventario()
        self.cargar_inventario()

    def cargar_inventario(self) -> None:
        """Carga el inventario al iniciar el programa"""
        if self.inventario.cargar_desde_archivo():
            print("Inventario cargado exitosamente.")
        else:
            print("No se encontró archivo de inventario. Se creará uno nuevo.")

    def guardar_inventario(self) -> None:
        """Guarda el inventario antes de salir"""
        if self.inventario.guardar_a_archivo():
            print("Inventario guardado exitosamente.")
        else:
            print("Error al guardar el inventario.")

    def mostrar_menu(self) -> None:
        """Muestra el menú principal"""
        print("\n" + "=" * 50)
        print("SISTEMA DE GESTIÓN DE INVENTARIO")
        print("=" * 50)
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar y salir")
        print("=" * 50)

    def añadir_producto(self) -> None:
        """Interfaz para añadir un nuevo producto"""
        print("\n--- Añadir Nuevo Producto ---")

        try:
            id = int(input("ID del producto: "))
            nombre = input("Nombre del producto: ").strip()
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))

            producto = Producto(id, nombre, cantidad, precio)

            if self.inventario.añadir_producto(producto):
                print("Producto añadido exitosamente.")
            else:
                print("Error: El ID ya existe.")

        except ValueError:
            print("Error: Ingrese valores numéricos válidos para ID, cantidad y precio.")

    def eliminar_producto(self) -> None:
        """Interfaz para eliminar un producto"""
        print("\n--- Eliminar Producto ---")

        try:
            id = int(input("ID del producto a eliminar: "))

            if self.inventario.eliminar_producto(id):
                print("Producto eliminado exitosamente.")
            else:
                print("Error: Producto no encontrado.")

        except ValueError:
            print("Error: Ingrese un ID válido.")

    def actualizar_producto(self) -> None:
        """Interfaz para actualizar un producto"""
        print("\n--- Actualizar Producto ---")

        try:
            id = int(input("ID del producto a actualizar: "))

            producto = self.inventario.obtener_producto_por_id(id)
            if not producto:
                print("Error: Producto no encontrado.")
                return

            print(f"Producto actual: {producto}")

            print("\n¿Qué desea actualizar?")
            print("1. Cantidad")
            print("2. Precio")
            print("3. Ambos")

            opcion = input("Seleccione una opción (1-3): ").strip()

            cantidad = None
            precio = None

            if opcion in ['1', '3']:
                cantidad = int(input("Nueva cantidad: "))

            if opcion in ['2', '3']:
                precio = float(input("Nuevo precio: "))

            if self.inventario.actualizar_producto(id, cantidad, precio):
                print("Producto actualizado exitosamente.")
            else:
                print("Error al actualizar el producto.")

        except ValueError:
            print("Error: Ingrese valores válidos.")

    def buscar_producto(self) -> None:
        """Interfaz para buscar productos por nombre"""
        print("\n--- Buscar Producto por Nombre ---")

        nombre = input("Nombre a buscar: ").strip()

        if not nombre:
            print("❌ Error: Ingrese un nombre para buscar.")
            return

        resultados = self.inventario.buscar_por_nombre(nombre)

        if resultados:
            print(f"\n {len(resultados)} producto(s) encontrado(s):")
            for producto in resultados:
                print(f"   - {producto}")
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos_productos(self) -> None:
        """Muestra todos los productos del inventario"""
        print("\n--- Todos los Productos ---")

        productos = self.inventario.mostrar_todos()

        if productos:
            for producto in productos:
                print(producto)
            print(f"\nTotal de productos: {len(productos)}")
        else:
            print("El inventario está vacío.")

    def ejecutar(self) -> None:
        """Método principal que ejecuta el sistema"""
        while True:
            self.mostrar_menu()

            opcion = input("Seleccione una opción (1-6): ").strip()

            if opcion == '1':
                self.añadir_producto()
            elif opcion == '2':
                self.eliminar_producto()
            elif opcion == '3':
                self.actualizar_producto()
            elif opcion == '4':
                self.buscar_producto()
            elif opcion == '5':
                self.mostrar_todos_productos()
            elif opcion == '6':
                self.guardar_inventario()
                print(" ¡Hasta luego!")
                break
            else:
                print(" Opción no válida. Intente nuevamente.")

            input("\nPresione Enter para continuar...")


# Punto de entrada del programa
if __name__ == "__main__":
    sistema = SistemaInventario()
    sistema.ejecutar()