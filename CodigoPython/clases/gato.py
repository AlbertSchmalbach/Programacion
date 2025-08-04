# Crea una subclase `Gato` que hereda de `Animal`, añade el atributo `color`, y sobreescribe el método `hacer_sonido`.
from animal import Animal

class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def hacer_sonido(self):
        return f'{self.nombre} es un gato y hace miauu'
    
# 4. Crea instancias de `Perro` y `Gato` y haz que emitan sus sonidos.

gato1 = Gato('Felix', 1, 'Tuxedo')
# print(gato1.hacer_sonido())

print(gato1.presentar_animal())