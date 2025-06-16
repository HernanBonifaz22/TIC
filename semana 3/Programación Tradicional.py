# Programa para calcular promedio semanal de temperatura - programacion tradicional

def ingresar_datos():
    """Solicita temperaturas para 7 días"""
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    temperaturas = []

    print("➤ Ingrese temperaturas en °C")
    for dia in dias:
        while True:
            try:
                temp = float(input(f"{dia}: "))
                temperaturas.append(temp)
                break
            except:
                print("¡Error! Ingrese un número válido")

    return temperaturas


def calcular_promedio(temps):
    """Calcula el promedio de temperaturas"""
    return sum(temps) / len(temps)


def mostrar_analisis(temps):
    """Muestra resultados completos"""
    promedio = calcular_promedio(temps)
    max_temp = max(temps)
    min_temp = min(temps)

    print("\n" + "═" * 40)
    print(f" Análisis Semanal".center(40))
    print("═" * 40)
    print(f"• Promedio: {promedio:.1f}°C")
    print(f"• Máxima:   {max_temp}°C")
    print(f"• Mínima:   {min_temp}°C")
    print("═" * 40)


# --- Ejecución principal ---
if __name__ == "__main__":
    print("CALCULADORA DE TEMPERATURAS SEMANALES")
    datos = ingresar_datos()
    mostrar_analisis(datos)