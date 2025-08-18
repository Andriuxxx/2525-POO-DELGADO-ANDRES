# Clase que representa un producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos para actualizar los atributos
    def actualizar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    # Representación del producto
    def __str__(self):
        return f"[{self.id}] {self.nombre} - Cantidad: {self.cantidad} - Precio: ${self.precio:.2f}"


# Clase que maneja el inventario
class Inventario:
    def __init__(self):
        self.productos = []

    # Añadir producto asegurando ID único
    def agregar_producto(self, producto):
        if any(p.id == producto.id for p in self.productos):
            print("Ya existe un producto con ese ID. Intenta con otro.")
            return
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado correctamente.")

    # Eliminar producto por ID
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.id == id_producto:
                self.productos.remove(p)
                print(f"Producto '{p.nombre}' eliminado.")
                return
        print("No se encontró un producto con ese ID.")

    # Actualizar cantidad y/o precio
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.id == id_producto:
                if cantidad is not None:
                    p.actualizar_cantidad(cantidad)
                if precio is not None:
                    p.actualizar_precio(precio)
                print(f"Producto '{p.nombre}' actualizado correctamente.")
                return
        print("No se encontró un producto con ese ID.")

    # Buscar productos por nombre (puede ser parcial)
    def buscar_producto(self, texto):
        resultados = [p for p in self.productos if texto.lower() in p.nombre.lower()]
        if resultados:
            print("Productos encontrados:")
            for p in resultados:
                print(p)
        else:
            print("No se encontró ningún producto con ese nombre.")

    # Mostrar todos los productos
    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
            return
        print("Inventario completo:")
        for p in self.productos:
            print(p)


# Menú principal
def menu():
    inv = Inventario()
    while True:
        print("\n===== Sistema de Inventario =====")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            id_prod = input("ID del producto: ")
            nombre = input("Nombre: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
            except ValueError:
                print("Cantidad o precio inválidos, intenta de nuevo.")
                continue
            prod = Producto(id_prod, nombre, cantidad, precio)
            inv.agregar_producto(prod)

        elif opcion == "2":
            id_prod = input("ID del producto a eliminar: ")
            inv.eliminar_producto(id_prod)

        elif opcion == "3":
            id_prod = input("ID del producto a actualizar: ")
            cant = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            cant_val = int(cant) if cant else None
            precio_val = float(precio) if precio else None
            inv.actualizar_producto(id_prod, cant_val, precio_val)

        elif opcion == "4":
            texto = input("Ingresa el nombre o parte del nombre a buscar: ")
            inv.buscar_producto(texto)

        elif opcion == "5":
            inv.mostrar_inventario()

        elif opcion == "6":
            print("Saliendo... ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intenta otra vez.")


if __name__ == "__main__":
    menu()
