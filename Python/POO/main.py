from persona import Persona
from atm import Atm

# CLASE PERSONA

# persona1 = Persona("Luz Saray", 23)
# print(persona1)
# persona1.saludar()
# persona2 = Persona("Misuris Paola", 18)
# print(persona2)
# persona3 = Persona("Maria Camila", 25)
# print(persona3)
# del persona3.nombre
# del persona3
# print(persona3) #"Error persona3 no esta definida"

# CLASE CAJERO AUTOMATICO

pin = input("Ingresa tu pin: ")

# Crear el objeto una sola vez
atm = Atm(pin)

while True:


    user_input = input(
    """ ¿Que proceso desea realizar?

        1. Ingresa 1 para cambiar el pin
        2. Ingresa 2 para depositar
        3. Ingresa 3 para retirar
        4. Ingresa 4 para consultar tu saldo
        5. Ingresa 5 para salir del programa

    Por favor digite la opcion deseada: """
    )

    match user_input:

        case "1":
            print(pin)
            new_pin = input("Ingresa el nuevo pin: ")
            print(new_pin)
            atm.change_pin(new_pin)

        case "2":
            amount = float(input("Ingresa el saldo a depositar: "))
            atm.deposit(amount)

        case "3":
            money_withdraw = float(input("Ingresa el saldo a retirar: "))
            atm.withdraw(money_withdraw)

        case "4":
            atm.show_balance()

        case "5":
            print("Saliendo del programa...")
            break

        case _:
            print("Opcion no valida")