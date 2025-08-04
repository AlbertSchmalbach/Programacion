class Padre:
    def __init__(self, atributo_padre):
        self.atributo_padre = atributo_padre

    def metodo_padre(self):
        return "Método padre"

class Hija(Padre):
    def __init__(self, atributo_hija, atributo_padre):
        super().__init__(atributo_padre)
        self.atributo_hija = atributo_hija

    def metodo_hija(self):
        return "Método hija"
    
# padre = Padre('Padre')
# hija = Hija('Hija', 'Padre')
# print(hija.metodo_padre())

class FamiliaProgramadores:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print("Hola, soy", self.nombre, "y soy un programador.")

    def trabajar(self):
        print("Estoy trabajando en un proyecto emocionante!")

class HijoProgramador(FamiliaProgramadores):
    def __init__(self, nombre, lenguaje):
        super().__init__(nombre)
        self.lenguaje = lenguaje

    def programar(self):
        print("Estoy programando en", self.lenguaje)

    def jugar(self):
        print("¡Hora de jugar a mi videojuego!")

hijo = HijoProgramador("Alberto", "Python")
hijo.saludar()    # Salida: Hola, soy Juan y soy un programador.
hijo.programar()  # Salida: Estoy programando en Python
hijo.trabajar()   # Salida: Estoy trabajando en un proyecto emocionante!
hijo.jugar()      # Salida: ¡Hora de jugar a mi videojuego!

# Herencia multiple

class Padre1:
    def metodo_padre1(self):
        return "Método padre 1"

class Padre2:
    def metodo_padre2(self):
        return "Método padre 2"

class Hija(Padre1, Padre2):
    pass


# padre1 = Padre1()
# padre2 = Padre2()
# hija = Hija()
# print(hija.metodo_padre2())

