# 2. Crea una subclase `Perro` que hereda de `Animal`, añade el atributo `raza`, y sobreescribe el método `hacer_sonido`.

from animal import Animal

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        return f'{self.nombre} es un perro y hace guauu'
    
# 4. Crea instancias de `Perro` y `Gato` y haz que emitan sus sonidos.    

perro1 = Perro('Firulais', 2, 'Pastor Aleman')
# print(perro1.hacer_sonido())

print(perro1.presentar_animal())