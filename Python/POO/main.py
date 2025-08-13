# Crear una Clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}"
    
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}\n")

# Crear un Objeto
persona1 = Persona("Luz Saray", 23)
print(persona1)
persona1.saludar()
# persona2 = Persona("Misuris Paola", 18)
# print(persona2)
persona3 = Persona("Maria Camila", 25)
print(persona3)
del persona3.nombre
del persona3
# print(persona3) #"Error persona3 no esta definida"
    