"""
Programa para convertir Unidades de Medida

Este programa sirve para convertir entre diferentes unidades de medida:
- Longitud (metros, pies, pulgadas, yardas)
- Peso (kilogramos, libras, onzas)
- Temperatura (Celsius, Fahrenheit, Kelvin)
- Volumen (litros, galones, mililitros)

El usuario selecciona la categoría y las unidades específicas para la conversión.
"""


def convertir_longitud():
    """Convierte entre unidades de longitud"""
    print("\nOpciones de longitud:")
    print("1. Metros a Pies")
    print("2. Pies a Metros")
    print("3. Pulgadas a Centímetros")
    print("4. Yardas a Metros")

    opcion = int(input("Seleccione una opción (1-4): "))
    valor = float(input("Ingrese el valor a convertir: "))

    if opcion == 1:
        resultado = valor * 3.28084
        print(f"{valor} metros = {resultado:.2f} pies")
    elif opcion == 2:
        resultado = valor / 3.28084
        print(f"{valor} pies = {resultado:.2f} metros")
    elif opcion == 3:
        resultado = valor * 2.54
        print(f"{valor} pulgadas = {resultado:.2f} centímetros")
    elif opcion == 4:
        resultado = valor * 0.9144
        print(f"{valor} yardas = {resultado:.2f} metros")
    else:
        print("Opción no válida")


def convertir_peso():
    """Convierte entre unidades de peso"""
    print("\nOpciones de peso:")
    print("1. Kilogramos a Libras")
    print("2. Libras a Kilogramos")
    print("3. Onzas a Gramos")

    opcion = int(input("Seleccione una opción (1-3): "))
    valor = float(input("Ingrese el valor a convertir: "))

    if opcion == 1:
        resultado = valor * 2.20462
        print(f"{valor} kg = {resultado:.2f} libras")
    elif opcion == 2:
        resultado = valor / 2.20462
        print(f"{valor} libras = {resultado:.2f} kg")
    elif opcion == 3:
        resultado = valor * 28.3495
        print(f"{valor} onzas = {resultado:.2f} gramos")
    else:
        print("Opción no válida")


def convertir_temperatura():
    """Convierte entre unidades de temperatura"""
    print("\nOpciones de temperatura:")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Celsius a Kelvin")

    opcion = int(input("Seleccione una opción (1-3): "))
    valor = float(input("Ingrese la temperatura a convertir: "))

    if opcion == 1:
        resultado = (valor * 9 / 5) + 32
        print(f"{valor}°C = {resultado:.2f}°F")
    elif opcion == 2:
        resultado = (valor - 32) * 5 / 9
        print(f"{valor}°F = {resultado:.2f}°C")
    elif opcion == 3:
        resultado = valor + 273.15
        print(f"{valor}°C = {resultado:.2f} K")
    else:
        print("Opción no válida")


def convertir_volumen():
    """Convierte entre unidades de volumen"""
    print("\nOpciones de volumen:")
    print("1. Litros a Galones")
    print("2. Galones a Litros")
    print("3. Mililitros a Onzas líquidas")

    opcion = int(input("Seleccione una opción (1-3): "))
    valor = float(input("Ingrese el valor a convertir: "))

    if opcion == 1:
        resultado = valor * 0.264172
        print(f"{valor} litros = {resultado:.2f} galones")
    elif opcion == 2:
        resultado = valor / 0.264172
        print(f"{valor} galones = {resultado:.2f} litros")
    elif opcion == 3:
        resultado = valor * 0.033814
        print(f"{valor} ml = {resultado:.2f} onzas líquidas")
    else:
        print("Opción no válida")


def main():
    """Función principal del programa"""
    print("CONVERSOR DE UNIDADES DE MEDIDA")

    while True:
        print("\nCategorías disponibles:")
        print("1. Longitud")
        print("2. Peso")
        print("3. Temperatura")
        print("4. Volumen")
        print("5. Salir")

        categoria = input("\nSeleccione una categoría (1-5): ")

        if categoria == '1':
            convertir_longitud()
        elif categoria == '2':
            convertir_peso()
        elif categoria == '3':
            convertir_temperatura()
        elif categoria == '4':
            convertir_volumen()
        elif categoria == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()