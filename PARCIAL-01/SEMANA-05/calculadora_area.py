# Programa que calcula el área de un triángulo o rectángulo usando POO.

class FiguraGeometrica:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        raise NotImplementedError("Este método debe ser implementado en las subclases.")


class Triangulo(FiguraGeometrica):
    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2


class Rectangulo(FiguraGeometrica):
    def calcular_area(self) -> float:
        return self.base * self.altura


def main():
    print("Bienvenido a la calculadora de áreas (POO)")
    print("Selecciona una figura para calcular su área:")
    print("1. Triángulo")
    print("2. Rectángulo")

    # Entrada como número para evitar errores de escritura
    opcion = input("Ingresa 1 o 2: ").strip()

    if opcion == "1":
        figura_nombre = "triángulo"
        base = float(input("Ingresa la base del triángulo (en cm): "))
        altura = float(input("Ingresa la altura del triángulo (en cm): "))
        figura_objeto = Triangulo(base, altura)

    elif opcion == "2":
        figura_nombre = "rectángulo"
        base = float(input("Ingresa la base del rectángulo (en cm): "))
        altura = float(input("Ingresa la altura del rectángulo (en cm): "))
        figura_objeto = Rectangulo(base, altura)

    else:
        print("Opción no válida. Debes ingresar 1 o 2.")
        return

    area = figura_objeto.calcular_area()
    print(f"\nEl área del {figura_nombre} es: {area:.2f} cm²")

    es_area_grande = area > 100
    if es_area_grande:
        print("¡El área calculada es bastante grande!")
    else:
        print("Área calculada correctamente.")


if __name__ == "__main__":
    main()
