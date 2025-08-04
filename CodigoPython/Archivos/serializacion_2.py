import pickle

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        return f'El {self.nombre} emite un sonido'
    
    def presentar_animal(self):
        return f'Animal: {self.nombre} - Edad: {self.edad} - Sonido: {self.hacer_sonido()}'

animal1 = Animal("Conejo", 5)
animal2 = Animal("Perro", 12)
animal3 = Animal("Gato", 8)

animales = [animal1, animal2, animal3]

fichero = open("animales", "wb")

pickle.dump(animales, fichero)

fichero.close()

del (fichero)

ficheroApertura = open("animales", "rb")

misAnimals = pickle.load(ficheroApertura)

ficheroApertura.close()

for animal in misAnimals:
    print(animal.presentar_animal())