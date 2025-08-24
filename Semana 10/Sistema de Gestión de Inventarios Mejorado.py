import os
import json
from datetime import datetime


class Producto:
    """Clase que representa un producto en el inventario"""

    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    def to_dict(self):
        """Convierte el producto a un diccionario para serialización"""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'cantidad': self.cantidad,
            'precio': self.precio
        }

    @classmethod
    def from_dict(cls, data):
        """Crea un producto desde un diccionario"""
        return cls(data['id'], data['nombre'], data['cantidad'], data['precio'])


class Inventario:
    """Clase que gestiona el inventario de productos con persistencia en archivo"""

    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga el inventario desde el archivo, manejando posibles excepciones"""
        try:
            # Verificar si el archivo existe
            if not os.path.exists(self.archivo):
                print("Archivo de inventario no encontrado. Se creará uno nuevo.")
                self.guardar_inventario()  # Crear archivo vacío
                return

            # Verificar permisos de lectura
            if not os.access(self.archivo, os.R_OK):
                raise PermissionError("No se tienen permisos de lectura para el archivo")

            with open(self.archivo, 'r', encoding='utf-8') as file:
                contenido = file.read().strip()

                # Manejar archivo vacío
                if not contenido:
                    print("Archivo de inventario está vacío.")
                    return

                try:
                    datos = json.loads(contenido)
                    for producto_data in datos:
                        producto = Producto.from_dict(producto_data)
                        self.productos[producto.id] = producto

                    print(f" Inventario cargado exitosamente desde {self.archivo}")
                    print(f" Productos cargados: {len(self.productos)}")

                except json.JSONDecodeError:
                    print("Error: El archivo de inventario está corrupto o tiene formato incorrecto")
                    print("Se creará un nuevo archivo de inventario")
                    self.productos = {}
                    self.guardar_inventario()

        except FileNotFoundError:
            print(f"Error: El archivo {self.archivo} no fue encontrado")
            print("Creando nuevo archivo de inventario...")
            self.guardar_inventario()

        except PermissionError as e:
            print(f"Error de permisos: {e}")
            print("El inventario se cargará en memoria pero los cambios no se guardarán")

        except Exception as e:
            print(f"Error inesperado al cargar el inventario: {e}")
            print("Continuando con inventario vacío")

    def guardar_inventario(self):
        """Guarda el inventario en el archivo, manejando posibles excepciones"""
        try:
            # Verificar permisos de escritura
            directorio = os.path.dirname(self.archivo) or '.'
            if not os.access(directorio, os.W_OK):
                raise PermissionError("No se tienen permisos de escritura en el directorio")

            # Convertir productos a lista de diccionarios
            productos_data = [producto.to_dict() for producto in self.productos.values()]

            with open(self.archivo, 'w', encoding='utf-8') as file:
                json.dump(productos_data, file, indent=2, ensure_ascii=False)

            print(f"Inventario guardado exitosamente en {self.archivo}")
            return True

        except PermissionError as e:
            print(f" Error de permisos al guardar: {e}")
            print("Los cambios no se han guardado en el archivo")
            return False

        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")
            return False

    def añadir_producto(self, id, nombre, cantidad, precio):
        """Añade un nuevo producto al inventario y guarda en archivo"""
        try:
            if id in self.productos:
                print("Error: Ya existe un producto con ese ID")
                return False

            # Validar datos de entrada
            if cantidad < 0 or precio < 0:
                print(" Error: La cantidad y el precio deben ser valores positivos")
                return False

            producto = Producto(id, nombre, cantidad, precio)
            self.productos[id] = producto

            # Intentar guardar en archivo
            if self.guardar_inventario():
                print(f"Producto '{nombre}' añadido exitosamente")
                return True
            else:
                print(" Producto añadido en memoria pero no guardado en archivo")
                return False

        except Exception as e:
            print(f"Error al añadir producto: {e}")
            return False

    def eliminar_producto(self, id):
        """Elimina un producto del inventario y actualiza el archivo"""
        try:
            if id not in self.productos:
                print("Error: No existe un producto con ese ID")
                return False

            nombre = self.productos[id].nombre
            del self.productos[id]

            if self.guardar_inventario():
                print(f"Producto '{nombre}' eliminado exitosamente")
                return True
            else:
                print("Producto eliminado de memoria pero no guardado en archivo")
                return False

        except Exception as e:
            print(f" Error al eliminar producto: {e}")
            return False

    def actualizar_producto(self, id, cantidad=None, precio=None):
        """Actualiza un producto existente y guarda los cambios"""
        try:
            if id not in self.productos:
                print("Error: No existe un producto con ese ID")
                return False

            producto = self.productos[id]
            cambios = []

            if cantidad is not None:
                if cantidad < 0:
                    print("Error: La cantidad debe ser un valor positivo")
                    return False
                producto.cantidad = cantidad
                cambios.append(f"cantidad a {cantidad}")

            if precio is not None:
                if precio < 0:
                    print("Error: El precio debe ser un valor positivo")
                    return False
                producto.precio = precio
                cambios.append(f"precio a ${precio:.2f}")

            if cambios:
                if self.guardar_inventario():
                    print(f" Producto '{producto.nombre}' actualizado: {', '.join(cambios)}")
                    return True
                else:
                    print(" Producto actualizado en memoria pero no guardado en archivo")
                    return False
            else:
                print("No se especificaron cambios para el producto")
                return False

        except Exception as e:
            print(f"Error al actualizar producto: {e}")
            return False

    def buscar_producto(self, nombre):
        """Busca productos por nombre"""
        encontrados = []
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                encontrados.append(producto)
        return encontrados

    def mostrar_inventario(self):
        """Muestra todos los productos del inventario"""
        if not self.productos:
            print(" El inventario está vacío")
            return

        print("\n" + "=" * 60)
        print("INVENTARIO ACTUAL")
        print("=" * 60)
        for producto in self.productos.values():
            print(f"  {producto}")
        print(f"\nTotal de productos: {len(self.productos)}")
        print("=" * 60)


def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n" + "=" * 60)
    print("SISTEMA DE GESTIÓN DE INVENTARIOS")
    print("=" * 60)
    print("1.  Añadir producto")
    print("2.   Eliminar producto")
    print("3.   Actualizar producto")
    print("4.  Buscar producto")
    print("5.  Mostrar inventario")
    print("6.  Guardar inventario (manual)")
    print("7.  Salir")
    print("=" * 60)


def main():
    """Función principal del programa"""
    print("Iniciando sistema de gestión de inventarios...")

    # Crear instancia del inventario (automáticamente carga desde archivo)
    inventario = Inventario()

    while True:
        try:
            mostrar_menu()
            opcion = input("\n Seleccione una opción (1-7): ").strip()

            if opcion == '1':
                print("\n➕ AÑADIR NUEVO PRODUCTO")
                try:
                    id = input("ID del producto: ").strip()
                    nombre = input("Nombre: ").strip()
                    cantidad = int(input("Cantidad: ").strip())
                    precio = float(input("Precio: ").strip())

                    if not id or not nombre:
                        print("Error: ID y Nombre son campos obligatorios")
                        continue

                    inventario.añadir_producto(id, nombre, cantidad, precio)

                except ValueError:
                    print(" Error: Cantidad y Precio deben ser números válidos")
                except Exception as e:
                    print(f" Error inesperado: {e}")

            elif opcion == '2':
                print("\n  ELIMINAR PRODUCTO")
                id = input("ID del producto a eliminar: ").strip()
                inventario.eliminar_producto(id)

            elif opcion == '3':
                print("\n ACTUALIZAR PRODUCTO")
                try:
                    id = input("ID del producto a actualizar: ").strip()

                    print("Deje en blanco los campos que no desea cambiar:")
                    cantidad_str = input("Nueva cantidad: ").strip()
                    precio_str = input("Nuevo precio: ").strip()

                    cantidad = int(cantidad_str) if cantidad_str else None
                    precio = float(precio_str) if precio_str else None

                    inventario.actualizar_producto(id, cantidad, precio)

                except ValueError:
                    print(" Error: Cantidad y Precio deben ser números válidos")

            elif opcion == '4':
                print("\n BUSCAR PRODUCTO")
                nombre = input("Nombre a buscar: ").strip()
                resultados = inventario.buscar_producto(nombre)

                if resultados:
                    print(f"\n Encontrados {len(resultados)} producto(s):")
                    for producto in resultados:
                        print(f"  {producto}")
                else:
                    print(" No se encontraron productos con ese nombre")

            elif opcion == '5':
                inventario.mostrar_inventario()

            elif opcion == '6':
                print("\n GUARDADO MANUAL")
                if inventario.guardar_inventario():
                    print(" Inventario guardado manualmente")
                else:
                    print(" Error al guardar el inventario")

            elif opcion == '7':
                print("\n Guardando cambios antes de salir...")
                inventario.guardar_inventario()
                print(" ¡Hasta pronto!")
                break

            else:
                print("Opción no válida. Por favor, seleccione 1-7")

        except KeyboardInterrupt:
            print("\n\n Interrupción detectada. Guardando y saliendo...")
            inventario.guardar_inventario()
            print("¡Hasta pronto!")
            break

        except Exception as e:
            print(f" Error inesperado en el menú: {e}")
            print("Continuando con la ejecución...")


if __name__ == "__main__":
    main()