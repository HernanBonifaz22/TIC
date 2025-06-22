
class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool = True):
        self.__titulo = titulo  # Nota: __titulo (con doble underscore)
        self.__autor = autor
        self.__isbn = isbn
        self.__disponible = disponible

    @property
    def titulo(self):
        return self.__titulo

    def marcar_prestado(self):
        if not self.__disponible:
            raise ValueError("El libro ya está prestado")
        self.__disponible = False

    def marcar_devuelto(self):  # Corregido "devoutio" -> "devuelto"
        self.__disponible = True

    def __str__(self):
        return f"'{self.titulo}' por {self.__autor} ({'Disponible' if self.__disponible else 'Prestado'})"


# Prueba
if __name__ == '__main__':
    libro = Libro("Cien años de soledad", "García Márquez", "123-456")  # libro con minúscula
    print(libro)
    libro.marcar_prestado()
    print(libro)