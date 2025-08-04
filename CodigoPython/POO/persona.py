class Persona:
    id = 0
    def __init__(self, nombre, bautizado=True):
        Persona.id += 1
        self.id_persona = Persona.id
        self.nombre = nombre
        self.bautizado = bautizado
        self.privilegio = "Sin privilegios"

    def asignar_privilegio(self):
        print(f'Publicador: {self.nombre}')
        if self.bautizado:
            self.privilegio = input("Cual es su privilegio?: ")            
        else:
            print('Aun no puede tener privilegios porque no esta bautizada') 
    
    def datos(self):
        print(f'''ID: {self.id_persona} 
              \nBautizado: {self.bautizado} 
              \nPrivilegio: {self.privilegio}''')


class Precursor(Persona):
    def __init__(self, nombre, tipo, bautizado=True):
        super().__init__(nombre, bautizado)
        self.tipo_precursor= tipo
        self.hora = 0
        self.escuela_precursor = ''

        if self.tipo_precursor == 'Regular':
            self.hora = 50
            print(self.nombre)
            self.escuela_precursor = input('Fue a las escuela de precursor? ')
        elif self.tipo_precursor == 'Auxiliar':
            self.hora = 30
            self.escuela_precursor = 'No aplica'
        else:
            print('No definido')

    def datos(self):
        print(f'''ID: {self.id_persona}
              \nNombre: {self.nombre} 
              \nPrecursor: {self.tipo_precursor} 
              \nHoras: {self.hora} 
              \nEscuela Precursor: {self.escuela_precursor}''')


# publicador1 = Persona('Alberto')
# publicador1.asignar_privilegio()
# print()
# print("DATOS DEL PUBLICADOR")
# publicador1.datos()
# print('------------------------------------------------------------------')
# print()

# publicador2 = Persona('Luz Saray')
# publicador2.asignar_privilegio()
# print()
# print("DATOS DEL PUBLICADOR")
# publicador2.datos()
# print('------------------------------------------------------------------')
# print()

# publicador3 = Persona('Melany', False)
# publicador3.asignar_privilegio()
# print()
# print("DATOS DEL PUBLICADOR")
# publicador3.datos()
# print('------------------------------------------------------------------')
# print()

precs1 = Precursor('Alberto', 'Regular')
precs2 = Precursor('Misuris Paola', 'Regular')
precs3 = Precursor('Bertha Isabel', 'Auxiliar')

# precs1.datos()
# print()
# precs2.datos()
# print()
# precs3.datos()
# print()

print(isinstance(precs2, Precursor))