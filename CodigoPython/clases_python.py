class Producto:

    contador = 0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.__precio = precio
        Producto.contador+= 1

    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    def __del__(self):
        print(f"Producto eliminado ✂: {self.nombre}")

    def __str__(self) -> str:
        return f"Nombre de producto: {self.nombre}"

    def info(self):
        print(f"{self.contador} - El producto {self.nombre} tiene por precio ${self.__precio} pesos")

    @classmethod
    def producto_default(cls):
        return cls("'nombreProducto'", 0)
    

producto1 = Producto.producto_default()
producto1.info()
producto2 = Producto("Smart TV", 2300000)
producto2.precio = 3000000
print(producto2.precio)
producto2.info()
print(producto2)
del producto1