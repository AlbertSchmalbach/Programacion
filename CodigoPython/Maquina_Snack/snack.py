class Snack:
    contador_snack = 0
    def __init__(self, nombre, precio):
        Snack.contador_snack+=1
        self.id = Snack.contador_snack
        self.nombre = nombre
        self.precio = precio

    def __str__(self) -> str:
        return f'Snack:\nId = {self.id}\nNombre = {self.nombre}\nPrecio = ${self.precio}'