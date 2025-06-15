# Descripción: Programa en el que se pide al usuario ingresar las temperaturas de una semana
# y se calcula el promedio usando funciones normales (sin clases ni objetos).

def pedir_temperaturas():
    """Función que pide al usuario que ingrese las temperaturas de los 7 días"""
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(lista_temperaturas):
    """Calcula el promedio de una lista de temperaturas"""
    total = sum(lista_temperaturas)
    return total / len(lista_temperaturas)

def main():
    print("Promedio Semanal del Clima (versión tradicional)")
    temps = pedir_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"El promedio de temperaturas es: {promedio:.2f} °C")

if __name__ == "__main__":
    main()
