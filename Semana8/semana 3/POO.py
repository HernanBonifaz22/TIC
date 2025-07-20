# Programa para calcular promedio semanal de temperatura - POO.

class AnalizadorClima:
    def __init__(self):
        self.dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        self.temperaturas = []

    def ingresar_datos(self):
        """Recolecta datos del usuario"""
        print("➤ Ingrese temperaturas en °C (POO)")
        for dia in self.dias:
            while True:
                try:
                    temp = float(input(f"{dia}: "))
                    self.temperaturas.append(temp)
                    break
                except:
                    print("¡Error! Ingrese un número válido")

    def calcular_promedio(self):
        """Calcula el promedio"""
        return sum(self.temperaturas) / len(self.temperaturas)

    def generar_reporte(self):
        """Muestra análisis completo"""
        print("\n" + "═" * 40)
        print(f"REPORTE CLIMÁTICO (POO)".center(40))
        print("═" * 40)
        print(f"• Días analizados: {len(self.dias)}")
        print(f"• Promedio: {self.calcular_promedio():.1f}°C")
        print(f"• Rango: {min(self.temperaturas)}°C a {max(self.temperaturas)}°C")
        print("═" * 40)


# --- Ejecución principal ---
if __name__ == "__main__":
    print("SISTEMA DE ANÁLISIS CLIMÁTICO (POO)")
    analizador = AnalizadorClima()
    analizador.ingresar_datos()
    analizador.generar_reporte()