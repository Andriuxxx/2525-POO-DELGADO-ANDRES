# Programa que demuestra el uso de constructores (__init__) y destructores (__del__) en Python.
# Simula la gestión de libros en una biblioteca. Al crear un objeto Libro, se inicializan sus atributos;
# al destruirlo, se imprime un mensaje simulando la devolución del libro o liberación de recursos.

class Libro:
    def __init__(self, titulo, autor, anio):
        """
        Constructor de la clase Libro.
        Se llama automáticamente al crear un objeto Libro.
        Inicializa los atributos con los valores proporcionados.
        """
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        print(f"Se ha registrado el libro: '{self.titulo}' de {self.autor} ({self.anio})")

    def mostrar_info(self):
        """Muestra la información del libro."""
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.anio}")

    def __del__(self):
        """
        Destructor de la clase Libro.
        Se llama automáticamente cuando el objeto es destruido.
        Simula liberar recursos (por ejemplo, devolver el libro a la estantería).
        """
        print(f"El libro '{self.titulo}' ha sido eliminado del sistema (liberación de recursos).")

# Código principal (punto de entrada del programa)
if __name__ == "__main__":
    print("Bienvenido al sistema de gestión de biblioteca\n")

    # Crear un objeto de tipo Libro
    libro1 = Libro("1984", "George Orwell", 1949)

    # Mostrar información del libro
    print("\nInformación del libro registrado:")
    libro1.mostrar_info()

    # Eliminar el objeto para activar el destructor manualmente
    print("\nEliminando el libro del sistema...")
    del libro1

    print("\nFin del programa.")
