class Productos:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self) -> str:
        return f"Producto: {self.nombre} - Precio: ${self.precio}"
    
class Categoria:

    productos = []

    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto):
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)


camiseta = Productos("T-Shirt", 35000)
jean = Productos("Jean-blue", 75000)
morral = Productos("Morral", 125000)

miscelaneo = Categoria("Miscelaneo", [camiseta, jean])
miscelaneo.agregar(morral)
miscelaneo.imprimir()