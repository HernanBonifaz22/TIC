# Clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self._id = id  # Atributo ID (único)
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio


# Clase Inventario
class Inventario:
    def __init__(self):
        self._productos = []  # Lista de productos

    # Añadir nuevo producto (asegurando que el ID sea único)
    def añadir_producto(self, producto):
        if not any(p.get_id() == producto.get_id() for p in self._productos):
            self._productos.append(producto)
            print(f"Producto {producto.get_nombre()} añadido con ID {producto.get_id()}.")
        else:
            print("Error: El ID ya existe.")

    # Actualizar cantidad o precio de un producto por ID
    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self._productos:
            if producto.get_id() == id:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print(f"Producto con ID {id} actualizado.")
                return
        print(f"Error: No se encontró producto con ID {id}.")

    # Buscar producto(s) por nombre (puede haber nombres similares)
    def buscar_productos(self, nombre):
        resultados = [p for p in self._productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for p in resultados:
                print(
                    f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    # Mostrar todos los productos en el inventario
    def mostrar_todos(self):
        if self._productos:
            for p in self._productos:
                print(
                    f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")
        else:
            print("El inventario está vacío.")


# Interfaz de consola
def main():
    inventario = Inventario()
    while True:
        print("\nOpciones:")
        print("1. Añadir producto")
        print("2. Actualizar producto")
        print("3. Buscar productos por nombre")
        print("4. Mostrar todos los productos")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            id = int(input("Ingrese ID: "))
            nombre = input("Ingrese nombre: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id = int(input("Ingrese ID del producto a actualizar: "))
            cantidad = input("Nueva cantidad (deje en blanco si no cambia): ")
            precio = input("Nuevo precio (deje en blanco si no cambia): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "3":
            nombre = input("Ingrese nombre a buscar: ")
            inventario.buscar_productos(nombre)

        elif opcion == "4":
            inventario.mostrar_todos()

        elif opcion == "5":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()