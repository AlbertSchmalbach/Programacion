# PROGRAMACION ORIENTADA A OBJETO

# CLASES
class Tarjeta:
    def __init__(self, numero, cantidad = 0):    # Inicializador
        self.numero = numero                        # Creación del atributo id  
        self.saldo = cantidad                # Creación del atributo saldo
        return
    
    def mostrar_saldo(self):
        print('El saldo es', self.saldo, '€')
        return
    
    def pagar(self, cantidad):
        self.saldo -= cantidad
        return
    
    def __str__(self):
        return 'Tarjeta número {} con saldo {:.2f}€'.format(self.numero, self.saldo)

# t = Tarjeta('0123456789', 1000)     # Creación de un objeto con argumentos             
# print(t)

# HERENCIA
class Tarjeta_descuento(Tarjeta):
    def __init__(self, id, descuento, cantidad = 0):
        self.id = id
        self.descuento = descuento
        self.saldo = cantidad
        return
    def mostrar_descuento(self):   # Método exclusivo de la clase Tarjeta_descuento
        print('Descuento de', self.descuento, '% en los pagos.')
        return
    
# POLIMORFISMO
class Tarjeta_Oro(Tarjeta):
    def __init__(self, id, descuento, cantidad = 0):
        self.id = id
        self.descuento = descuento
        self.saldo = cantidad
        return
    def pagar(self, cantidad):
        self.saldo -= cantidad * (1 - self.descuento / 100)
    
t1 = Tarjeta_descuento('0123456789', 2, 1000)
t1.pagar(100)
t1.mostrar_saldo()
t1.mostrar_descuento()
# print(isinstance(t1, Tarjeta))
# print(isinstance(t1, Tarjeta_descuento))

t2 = Tarjeta_Oro('2222222222', 1, 1000)
t2.pagar(100)
t2.mostrar_saldo()
                      
    
