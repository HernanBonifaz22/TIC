"""
Programa demostrativo de conceptos de POO en Python
Incluye herencia, encapsulación y polimorfismo
"""


# Clase base que representa un Vehículo
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self._marca = marca  # Atributo encapsulado (protected)
        self._modelo = modelo
        self._año = año
        self._kilometraje = 0  # Atributo encapsulado

    # Métodos getter para acceder a los atributos encapsulados
    def get_marca(self):
        return self._marca

    def get_modelo(self):
        return self._modelo

    def get_año(self):
        return self._año

    def get_kilometraje(self):
        return self._kilometraje

    # Método setter para modificar el kilometraje con validación
    def set_kilometraje(self, nuevo_kilometraje):
        if nuevo_kilometraje >= self._kilometraje:
            self._kilometraje = nuevo_kilometraje
        else:
            print("Error: El kilometraje no puede ser menor al actual")

    # Método que será sobrescrito en las clases hijas (polimorfismo)
    def descripcion(self):
        return f"{self._marca} {self._modelo} ({self._año}) - {self._kilometraje} km"

    # Método común a todos los vehículos
    def avanzar(self, kilometros):
        self._kilometraje += kilometros
        print(f"El vehículo ha avanzado {kilometros} km")


# Clase derivada que hereda de Vehículo (herencia)
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, num_puertas):
        super().__init__(marca, modelo, año)
        self.__num_puertas = num_puertas  # Atributo privado

    # Sobrescritura del método descripcion (polimorfismo)
    def descripcion(self):
        return f"{super().descripcion()}, {self.__num_puertas} puertas"

    # Método específico de Automovil
    def abrir_puertas(self):
        print(f"Abriendo {self.__num_puertas} puertas")


# Otra clase derivada que hereda de Vehículo
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)
        self.__tipo = tipo  # Atributo privado

    # Sobrescritura del método descripcion (polimorfismo)
    def descripcion(self):
        return f"{super().descripcion()}, tipo {self.__tipo}"

    # Método específico de Motocicleta
    def hacer_caballito(self):
        print("La motocicleta está haciendo un caballito!")


# Función que muestra polimorfismo al aceptar diferentes tipos de vehículos
def mostrar_info_vehiculo(vehiculo):
    print(vehiculo.descripcion())


# Ejemplo de uso del programa
if __name__ == "__main__":
    print("=== Demostración de conceptos de POO ===")

    # Creación de objetos
    auto = Automovil("Toyota", "Corolla", 2020, 4)
    moto = Motocicleta("Honda", "CBR600", 2019, "deportiva")

    # Uso de métodos y demostración de encapsulación
    auto.set_kilometraje(15000)
    auto.avanzar(200)

    moto.set_kilometraje(8000)
    moto.avanzar(150)

    # Demostración de polimorfismo
    print("\n=== Descripción de vehículos ===")
    mostrar_info_vehiculo(auto)
    mostrar_info_vehiculo(moto)

    # Uso de métodos específicos
    print("\n=== Acciones específicas ===")
    auto.abrir_puertas()
    moto.hacer_caballito()