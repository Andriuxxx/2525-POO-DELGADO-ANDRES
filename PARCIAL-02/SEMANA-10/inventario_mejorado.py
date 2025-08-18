import os

class Producto:
    def __init__(self, pid, nombre, cantidad, precio):
        self.id = pid
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}"


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar()

    def cargar(self):
        if not os.path.exists(self.archivo):
            open(self.archivo, "w").close()
            return
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    try:
                        pid, nombre, cantidad, precio = linea.strip().split(",")
                        self.productos[pid] = Producto(pid, nombre, int(cantidad), float(precio))
                    except ValueError:
                        print("⚠ Línea corrupta ignorada en archivo.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al leer archivo: {e}")

    def guardar(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos.values():
                    f.write(str(p) + "\n")
            return True
        except PermissionError:
            print("❌ No se pudo guardar, sin permisos.")
            return False

    def agregar(self, pid, nombre, cantidad, precio):
        if pid in self.productos:
            print("❌ ID repetido.")
            return
        self.productos[pid] = Producto(pid, nombre, cantidad, precio)
        if self.guardar():
            print("✔ Producto agregado.")

    def actualizar(self, pid, cantidad=None, precio=None):
        if pid not in self.productos:
            print("❌ Producto no encontrado.")
            return
        if cantidad is not None:
            self.productos[pid].cantidad = cantidad
        if precio is not None:
            self.productos[pid].precio = precio
        if self.guardar():
            print("✔ Producto actualizado.")

    def eliminar(self, pid):
        if pid in self.productos:
            del self.productos[pid]
            if self.guardar():
                print("✔ Producto eliminado.")
        else:
            print("❌ Producto no encontrado.")

    def mostrar(self):
        if not self.productos:
            print("Inventario vacío.")
            return
        for p in self.productos.values():
            print(f"{p.id} - {p.nombre} | Cant: {p.cantidad} | Precio: {p.precio}")


def menu():
    inv = Inventario()
    while True:
        print("\n--- Inventario ---")
        print("1. Ver productos")
        print("2. Agregar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        op = input("Opción: ")
        if op == "1":
            inv.mostrar()
        elif op == "2":
            pid = input("ID: ")
            nombre = input("Nombre: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inv.agregar(pid, nombre, cantidad, precio)
            except ValueError:
                print("❌ Datos inválidos.")
        elif op == "3":
            pid = input("ID a actualizar: ")
            try:
                cantidad = int(input("Nueva cantidad (vacío para no cambiar): ") or -1)
                precio = float(input("Nuevo precio (vacío para no cambiar): ") or -1)
                inv.actualizar(pid, None if cantidad == -1 else cantidad,
                               None if precio == -1 else precio)
            except ValueError:
                print("❌ Datos inválidos.")
        elif op == "4":
            pid = input("ID a eliminar: ")
            inv.eliminar(pid)
        elif op == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
