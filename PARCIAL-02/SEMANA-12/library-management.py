class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (autor, titulo)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[1]} por {self.info[0]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}     # ISBN -> Libro
        self.usuarios = {}               # ID -> Usuario
        self.ids_usuarios = set()        # IDs únicos
        self.historial_prestamos = {}    # ISBN -> Libro

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.info[1]}' agregado.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' registrado.")
        else:
            print(f"El ID {usuario.id_usuario} ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            if self.usuarios[id_usuario].libros_prestados:
                print("El usuario tiene libros prestados.")
            else:
                del self.usuarios[id_usuario]
                self.ids_usuarios.remove(id_usuario)
                print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, isbn, id_usuario):
        if isbn not in self.libros_disponibles:
            print("Libro no disponible.")
            return
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return
        libro = self.libros_disponibles.pop(isbn)
        self.usuarios[id_usuario].libros_prestados.append(isbn)
        self.historial_prestamos[isbn] = libro
        print(f"Libro '{libro.info[1]}' prestado a {self.usuarios[id_usuario].nombre}.")

    def devolver_libro(self, isbn, id_usuario):
        if id_usuario not in self.usuarios or isbn not in self.historial_prestamos:
            print("Datos no válidos.")
            return
        if isbn not in self.usuarios[id_usuario].libros_prestados:
            print("Este usuario no tiene este libro.")
            return
        libro = self.historial_prestamos.pop(isbn)
        self.libros_disponibles[isbn] = libro
        self.usuarios[id_usuario].libros_prestados.remove(isbn)
        print(f"Libro '{libro.info[1]}' devuelto por {self.usuarios[id_usuario].nombre}.")

    def buscar_libro(self, **kwargs):
        resultados = []
        for libro in self.libros_disponibles.values():
            if ('titulo' in kwargs and kwargs['titulo'].lower() in libro.info[1].lower()) or \
               ('autor' in kwargs and kwargs['autor'].lower() in libro.info[0].lower()) or \
               ('categoria' in kwargs and kwargs['categoria'].lower() in libro.categoria.lower()):
                resultados.append(libro)
        if resultados:
            print("Libros encontrados:")
            for l in resultados:
                print(f"- {l}")
        else:
            print("No se encontraron libros.")

    def listar_prestamos_usuario(self, id_usuario):
        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return
        usuario = self.usuarios[id_usuario]
        if not usuario.libros_prestados:
            print("No tiene libros prestados.")
        else:
            print(f"Libros prestados a {usuario.nombre}:")
            for isbn in usuario.libros_prestados:
                libro = self.historial_prestamos.get(isbn)
                if libro:
                    print(f"- {libro}")
                else:
                    print(f"- ISBN: {isbn}")


# Pruebas del sistema
biblioteca = Biblioteca()

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "12345")
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "Fábula", "67890")
libro3 = Libro("1984", "George Orwell", "Distopía", "54321")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

usuario1 = Usuario("Ana", "U001")
usuario2 = Usuario("Luis", "U002")

biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

biblioteca.prestar_libro("12345", "U001")
biblioteca.prestar_libro("67890", "U002")

biblioteca.listar_prestamos_usuario("U001")
biblioteca.listar_prestamos_usuario("U002")

biblioteca.buscar_libro(titulo="1984")
biblioteca.buscar_libro(autor="García")
biblioteca.buscar_libro(categoria="Distopía")

biblioteca.devolver_libro("12345", "U001")

biblioteca.dar_baja_usuario("U002")  # Aún tiene libros → no debería darse de baja
biblioteca.devolver_libro("67890", "U002")
biblioteca.dar_baja_usuario("U002")

biblioteca.quitar_libro("54321")
