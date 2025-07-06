# Programa que demuestra conceptos de POO (encapsulación, herencia y polimorfismo) con clases Instrumento y Guitarra

class Instrumento:
    def __init__(self, tipo):
        self.__tipo = tipo  # Atributo privado para encapsulación

    def tocar(self):
        return f"Tocando un {self.get_tipo()} genéricamente"

    def get_tipo(self):  # Método getter para acceder a __tipo
        return self.__tipo


class Guitarra(Instrumento):  # Herencia de Instrumento
    def __init__(self, tipo, cuerdas):
        super().__init__(tipo)
        self.__cuerdas = cuerdas  # Atributo privado adicional

    def tocar(self):  # Polimorfismo: sobrescribe el método tocar
        return f"Tocando una guitarra {self.get_tipo()} con {self.__cuerdas} cuerdas"

    def tocar_con_estilo(self, *estilos):  # Polimorfismo con argumentos múltiples
        if estilos:
            return f"Tocando guitarra {self.get_tipo()} con estilos: {', '.join(estilos)}"
        return f"Tocando guitarra {self.get_tipo()} sin estilo específico"


# Instancias y uso
mi_instrumento = Instrumento("percusión")
mi_guitarra = Guitarra("acústica", 6)

print(mi_instrumento.tocar())  # Uso de la clase base
print(mi_guitarra.tocar())     # Polimorfismo
print(mi_guitarra.tocar_con_estilo("rock", "clásico"))  # Argumentos múltiples
