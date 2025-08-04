class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )


class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

class Camioneta(Vehiculo):

    def __init__(self, color, ruedas, carga):
        super().__init__(color, ruedas)
        self.carga = carga

    def __str__(self):
        return super().__str__() + ", Capcidad: {} kg".format(self.carga)
    
class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ", Tipo: {} ".format(self.tipo)
    
class Motocicleta(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)


def catalogar(vehiculos, ruedas=None):
    contador = 0
    for vehiculo in vehiculos:
        if ruedas == vehiculo.ruedas:
            print(f"Clase: {type(vehiculo).__name__}")
            print("Atributos:")
            for atributo, valor in vehiculo.__dict__.items():
                print(f"  {atributo}: {valor}") 
            print()
            contador+=1
        else:
            print(f"Clase: {type(vehiculo).__name__}")
            print("Atributos:")
            for atributo, valor in vehiculo.__dict__.items():
                print(f"  {atributo}: {valor}") 
            print()

                
    
    if ruedas:
       print(f"Se han encontrado {contador} vehículos con {ruedas} ruedas:")
            

coche = Coche("azul", 4, 150, 1200)
camioneta = Camioneta('Blanca', 4, 1120)
bicicleta = Bicicleta("Negra", 2, "Todoterreno")
motocicleta = Motocicleta("Azul", 2, 120, 149)

vehiculos = [coche, camioneta, bicicleta, motocicleta]

catalogar(vehiculos, 2)

