import pickle

# Podemos guardar lo que queramos, listas, diccionarios, tuplas...
lista = [1,2,3,4,5]

# Escritura en modo binario, vacía el fichero si existe
fichero = open('lista.pckl','wb')

# Escribe la colección en el fichero 
pickle.dump(lista, fichero) 

# Lectura en modo binario 
fichero = open('lista.pckl','rb') 

# Cargamos los datos del fichero
lista_fichero = pickle.load(fichero)
print(lista_fichero)

fichero.close()

# Creamos una clase de prueba
class Persona:

    def __init__(self,nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

# Creamos la lista con los objetos
nombres = ["Alberto","Luz Saray","Milary"]
personas = []

for n in nombres:
    p = Persona(n)
    personas.append(p)

# Escribimos la lista en el fichero con pickle
import pickle
f = open('personas.pckl','wb')
pickle.dump(personas, f)
f.close()

# Leemos la lista del fichero con pickle
f = open('personas.pckl','rb')
personas = pickle.load(f)
f.close()

for p in personas:
    print(p)
