# 1. Crea una clase `Animal` con los atributos `nombre` y `edad`, y un método `hacer_sonido`.

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        return f'El {self.nombre} emite un sonido'
    
    def presentar_animal(self):
        return f'Animal: {self.nombre} - Edad: {self.edad} - Sonido: {self.hacer_sonido()}'






