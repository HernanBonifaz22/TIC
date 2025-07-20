"""
Programa de constructores (__init__) y destructores (__del__) en Python
"""

class Persona:
    """
    Clase que representa a una persona con nombre y edad.
    """

    def __init__(self, nombre, edad):
        """
        Constructor de la clase Persona.

        :param nombre: Nombre de la persona
        :param edad: Edad de la persona
        """
        self.nombre = nombre
        self.edad = edad
        print(f"Se ha creado una nueva persona: {self.nombre} ({self.edad} años)")

    def __del__(self):
        """
        Destructor de la clase Persona.
        """
        print(f"La persona {self.nombre} está siendo eliminada de la memoria")

    def presentarse(self):
        """Método para que la persona se presente"""
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")


class Archivo:
    """
    Clase que maneja archivos, demostrando el uso de destructores para liberar recursos.
    """

    def __init__(self, nombre_archivo):
        """
        Constructor que abre el archivo en modo lectura.

        :param nombre_archivo: Nombre del archivo a abrir
        """
        self.nombre = nombre_archivo
        self.archivo = open(nombre_archivo, 'r')
        print(f"Archivo {nombre_archivo} abierto correctamente")

    def leer(self):
        """Lee y muestra el contenido del archivo"""
        print("\nContenido del archivo:")
        print(self.archivo.read())

    def __del__(self):
        """
        Destructor que cierra el archivo cuando el objeto es destruido.
        """
        if hasattr(self, 'archivo') and not self.archivo.closed:
            self.archivo.close()
            print(f"Archivo {self.nombre} cerrado en el destructor")


def demostracion():
    """
    Función que demuestra el uso de las clases Persona y Archivo.
    """
    print("\n--- Creando objetos Persona ---")
    persona1 = Persona("Ana", 25)
    persona1.presentarse()

    persona2 = Persona("Carlos", 30)
    persona2.presentarse()

    print("\n--- Creando objeto Archivo ---")
    try:
        archivo = Archivo('ejemplo.txt')
        archivo.leer()
    except FileNotFoundError:
        print("\nError: Archivo no encontrado. Creando uno temporal para la demostración.")
        with open('ejemplo.txt', 'w') as f:
            f.write("Este es un archivo de ejemplo.\nLínea 2 del archivo.")
        archivo = Archivo('ejemplo.txt')
        archivo.leer()

    print("\n--- Fin de la función demostracion() ---")


if __name__ == "__main__":
    print("Inicio del programa")
    demostracion()

    print("\n--- Creando un objeto temporal ---")
    Persona("Temporal", 99)  # Objeto sin referencia

    print("\n--- Forzando la eliminación de un objeto ---")
    p = Persona("María", 40)
    del p  # Eliminación explícita

    print("\n--- Fin del programa ---")