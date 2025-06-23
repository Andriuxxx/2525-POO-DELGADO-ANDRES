# archivo: gestion_biblioteca.py

class Libro:
    def __init__(self, isbn, titulo, autor):
        """Inicializa un libro con ISBN, título y autor."""
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.prestado = False

    def prestar(self):
        """Marca el libro como prestado si está disponible."""
        if not self.prestado:
            self.prestado = True
            return f"Libro {self.titulo} prestado con éxito."
        return f"Libro {self.titulo} ya está prestado."

    def devolver(self):
        """Marca el libro como devuelto si estaba prestado."""
        if self.prestado:
            self.prestado = False
            return f"Libro {self.titulo} devuelto con éxito."
        return f"Libro {self.titulo} no estaba prestado."

class Usuario:
    def __init__(self, id_usuario, nombre):
        """Inicializa un usuario con ID y nombre."""
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.libros_prestados = []

    def prestar_libro(self, libro):
        """Permite al usuario prestar un libro."""
        resultado = libro.prestar()
        if "éxito" in resultado:
            self.libros_prestados.append(libro)
        return resultado

    def devolver_libro(self, libro):
        """Permite al usuario devolver un libro."""
        resultado = libro.devolver()
        if "éxito" in resultado:
            self.libros_prestados.remove(libro)
        return resultado

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un libro
    libro1 = Libro("123-456", "El Quijote", "Miguel de Cervantes")
    
    # Crear un usuario
    usuario1 = Usuario("U001", "María López")
    
    # Prestar y devolver un libro
    print(usuario1.prestar_libro(libro1))  # Presta el libro
    print(usuario1.prestar_libro(libro1))  # Intenta prestar de nuevo
    print(usuario1.devolver_libro(libro1))  # Devuelve el libro
