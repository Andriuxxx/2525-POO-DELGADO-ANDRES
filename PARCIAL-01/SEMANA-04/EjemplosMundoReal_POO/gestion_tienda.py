# archivo: gestion_tienda.py

class Producto:
    def __init__(self, codigo, nombre, precio):
        """Inicializa un producto con código, nombre y precio."""
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.disponible = True

    def vender(self):
        """Marca el producto como vendido si está disponible."""
        if self.disponible:
            self.disponible = False
            return f"Producto {self.nombre} vendido con éxito."
        return f"Producto {self.nombre} no está disponible."

    def reponer(self):
        """Repone el producto si estaba vendido."""
        if not self.disponible:
            self.disponible = True
            return f"Producto {self.nombre} repuesto con éxito."
        return f"Producto {self.nombre} ya está disponible."

class ClienteTienda:
    def __init__(self, id_cliente, nombre):
        """Inicializa un cliente con ID y nombre."""
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.compra = []

    def comprar(self, producto):
        """Permite al cliente comprar un producto."""
        resultado = producto.vender()
        if "éxito" in resultado:
            self.compra.append(producto)
        return resultado

    def devolver_compra(self, producto):
        """Permite al cliente devolver un producto."""
        resultado = producto.reponer()
        if "éxito" in resultado:
            self.compra.remove(producto)
        return resultado

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un producto
    producto1 = Producto("P001", "Laptop", 1200.0)
    
    # Crear un cliente
    cliente1 = ClienteTienda("C001", "Pedro Gómez")
    
    # Comprar y devolver un producto
    print(cliente1.comprar(producto1))  # Compra el producto
    print(cliente1.comprar(producto1))  # Intenta comprar de nuevo
    print(cliente1.devolver_compra(producto1))  # Devuelve el producto
