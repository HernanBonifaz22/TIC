from datetime import datetime, timedelta


class Prestamo:
    def __init__(self, libro, usuario):
        """
        Crea un nuevo préstamo relacionando un libro con un usuario
        :param libro: Objeto de la clase Libro
        :param usuario: Objeto de la clase Usuario (o sus subclases)
        """
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=15)
        libro.marcar_prestado()  # Cambia el estado del libro automáticamente

    def __str__(self):
        return f"Préstamo de '{self.libro.titulo}' a {self.usuario.nombre} (Devuelto antes de {self.fecha_devolucion.strftime('%d/%m/%Y')})"



if __name__ == "__main__":
    # Importaciones necesarias para la prueba
    from libro import Libro
    from usuario import Estudiante

    # Crear objetos de prueba
    libro_ejemplo = Libro("El Principito", "Antoine de Saint-Exupéry", "978-0156013926")
    estudiante_ejemplo = Estudiante("Juan Pérez", "E2024", "Literatura")

    # Crear préstamo
    prestamo = Prestamo(libro_ejemplo, estudiante_ejemplo)

    # Mostrar resultados
    print("\n--- Sistema de Préstamos POO ---\n")
    print(prestamo)
    print(f"Estado del libro: {libro_ejemplo}")