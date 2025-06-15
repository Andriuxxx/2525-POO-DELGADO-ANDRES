# Descripción: Programa que usa clases para guardar las temperaturas de la semana
# y calcular el promedio usando métodos de objetos.

class DiaClima:
    """Clase que guarda la temperatura de un solo día"""
    def __init__(self, temperatura):
        self.__temperatura = temperatura  # se usa __ para hacerlo privado

    def get_temperatura(self):
        return self.__temperatura

class SemanaClima:
    """Clase que representa toda la semana con sus temperaturas"""
    def __init__(self):
        self.lista_dias = []

    def agregar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            dia = DiaClima(temp)
            self.lista_dias.append(dia)

    def promedio_semanal(self):
        suma = 0
        for dia in self.lista_dias:
            suma += dia.get_temperatura()
        return suma / len(self.lista_dias)

def main():
    print("Promedio Semanal del Clima (versión POO)")
    semana = SemanaClima()
    semana.agregar_temperaturas()
    promedio = semana.promedio_semanal()
    print(f"El promedio de temperaturas es: {promedio:.2f} °C")

if __name__ == "__main__":
    main()
