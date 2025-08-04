import pickle
import os

class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print('Se ha creado una persona nueva con el nombre de: ', self.nombre)

    def __str__(self):
        # return '{} {} {}'.format(self.nombre, self.genero, self.edad)
        return f"{self.nombre} {self.genero} {self.edad}"


class ListaPersonas:

    personas = []

    def __init__(self):
        
        listaDePersonas = open("ficheroExterno", "ab+")
        listaDePersonas.seek(0)

        try:
            self.personas = pickle.load(listaDePersonas)
            if os.path.exists("ficheroExterno"):
                # print("Se cargaron {} personas del fichero externo".format(len(self.personas)+1))
                print(f"Se cargaron {len(self.personas)+1} personas del fichero externo")
        except:
            print("El fichero esta vacio")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self, persona):
        self.personas.append(persona)
        self.guardarPersonaFichero()

    def mostrarPersonas(self):
        for persona in self.personas:
            print(persona)

    def guardarPersonaFichero(self):
        listaDePersonas = open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarInfoFichero(self):
        print("La informacion del fichero externo es la siguiente:")
        for persona in self.personas:
            print(persona)

miLista = ListaPersonas()

# persona1 = Persona('Luz Saray', 'Femenenino', 23)
# miLista.agregarPersonas(persona1)

# persona2 = Persona('Misuris Paola', 'Femenenino', 18)
# miLista.agregarPersonas(persona2)

# persona3 = Persona('Luz Karime', 'Femenenino', 23)
# miLista.agregarPersonas(persona3)

# persona4 = Persona('Nazly', 'Femenenino', 26)
# miLista.agregarPersonas(persona4)

# persona5 = Persona('Maria Fernanda', 'Femenenino', 25)
# miLista.agregarPersonas(persona5)

miLista.mostrarInfoFichero()