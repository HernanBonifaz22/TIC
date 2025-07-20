from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nombre: str, id_usuario: str):
        self.nombre = nombre
        self.id = id_usuario

    @abstractmethod
    def tipo_usuario(self):
        pass


class Estudiante(Usuario):
    def __init__(self, nombre: str, id_estudiante: str, carrera: str):
        super().__init__(nombre, id_estudiante)
        self.carrera = carrera

    def tipo_usuario(self):
        return "Estudiante"


class Profesor(Usuario):
    def __init__(self, nombre: str, id_profesor: str, departamento: str):
        super().__init__(nombre, id_profesor)
        self.departamento = departamento

    def tipo_usuario(self):
        return "Profesor"



if __name__ == "__main__":
    print("\n--- Sistema de Usuarios POO ---\n")

    # Crear instancias
    estudiante1 = Estudiante("Ana López", "E2023", "Medicina")
    profesor1 = Profesor("Dr. García", "P101", "Biología")

    # Probar métodos
    print(f"{estudiante1.nombre}:")
    print(f"- Tipo: {estudiante1.tipo_usuario()}")
    print(f"- Carrera: {estudiante1.carrera}\n")

    print(f"{profesor1.nombre}:")
    print(f"- Tipo: {profesor1.tipo_usuario()}")
    print(f"- Departamento: {profesor1.departamento}\n")

    # Prueba de polimorfismo
    usuarios = [estudiante1, profesor1]
    print("Listado de usuarios:")
    for usuario in usuarios:
        print(f"• {usuario.id}: {usuario.nombre} ({usuario.tipo_usuario()})")