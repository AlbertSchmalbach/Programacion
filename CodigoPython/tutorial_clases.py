# CLASES, ENCAPSULACION
class Saludo:
    # Metodo constructor
    def __init__(self, nombre: str, apellido: str):
        self._nombre = nombre # Atributo protegido (un guion)
        self.__apellido = apellido # Atributo privado (dos guiones)
        print('Me acaban de instanciar 🤘')

    # Defino Getter
    @property
    def getApellido(self):
        return f'Tu apellido es {self.__apellido}'
    
    # Defino Setter
    @getApellido.setter
    def setApellido(self, NuevoApellido):
        if NuevoApellido != "":
            print("Modificando el valor")
            self.__apellido = NuevoApellido
        else:
            print("Error está vacío")

    def saludar(self):
        print(f'Hola {self._nombre} {self.__apellido}')
  
    def __del__(self):
        print('Este es mi fin')


saludando = Saludo('Albert', 'Lopez')
print(saludando._nombre)
# print(saludando._Saludo__apellido) # instancia + clase + atributo privado
saludando.setApellido = 'Schmalbach'
print(saludando.getApellido)
saludando.saludar()

# HERENCIA
class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):

    def __init__(self, lado):
        super().__init__(lado, lado)


if __name__ == '__main__':
    # rectangulo = Rectangulo(3, 4)
    # print(rectangulo.area())
    pass
    # cuadrado = Cuadrado(5)
    # print(cuadrado.area())

# POLIMORFISMO
class Vehiculo:

    def __init__(self, nombre):
        self.nombre = nombre

    def num_ruedas(self):
        pass

class Motocicleta(Vehiculo):
    def __init__(self):
        super().__init__('Motocicleta')

    def num_ruedas(self):
        return 2

if __name__ == "__main__":
    # moto = Motocicleta()
    # print(moto.num_ruedas())
    pass
