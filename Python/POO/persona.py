# Crear una Clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}"
    
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}\n")