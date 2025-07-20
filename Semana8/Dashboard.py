# Reemplaza todo el contenido con este código corregido:

import os
import subprocess


class Dashboard:
    def __init__(self):
        self.ruta_base = os.path.dirname(os.path.abspath(__file__))
        self.unidades = {
            '1': 'EjemplosMundoReal_POO',
            '2': 'semana 3',
            '3': 'Semana 5',
            '4': 'Semana 6',
            '5': 'Semana 7',
            '0': 'Salir'
        }

    def mostrar_contenido(self, ruta: str):
        try:
            print(f"\nContenido de {os.path.basename(ruta)}:")
            for item in sorted(os.listdir(ruta)):
                tipo = "[Carpeta]" if os.path.isdir(os.path.join(ruta, item)) else "[Archivo]"
                print(f"{tipo} {item}")
        except Exception as e:
            print(f"\nError al leer la carpeta: {e}")

    def mostrar_menu(self):
        while True:
            print("\n=== MENU PRINCIPAL ===")
            for key, value in self.unidades.items():
                print(f"{key}. {value}")

            opcion = input("\nSeleccione una opción (0 para salir): ")

            if opcion == '0':
                break

            if opcion in self.unidades:
                ruta = os.path.join(self.ruta_base, self.unidades[opcion])
                if os.path.exists(ruta):
                    self.mostrar_contenido(ruta)
                else:
                    print(f"\nLa ruta {ruta} no existe")


if __name__ == "__main__":
    Dashboard().mostrar_menu()