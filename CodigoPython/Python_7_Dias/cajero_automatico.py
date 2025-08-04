print('*** Cajero Automatico ***')

saldo = 500000
salir = False

while not salir:

    print('''
Operaciones que puedo realizar:
    1. Consultar Saldo
    2. Retirar
    3. Depositar
    4. Salir
''')
    opcion = int(input('Escoje una opcion: '))

    match opcion:
        case 1:
            print(f'Su saldo es de ${saldo}')
        case 2:
            retiro = int(input('Digite el monto a retirar: $'))
            saldo -= retiro
            print(f'Tu nuevo saldo es ${saldo}')
        case 3:
            deposito = int(input('Digite el monto a depositar: $'))
            saldo += deposito
            print(f'Tu nuevo saldo es ${saldo}')
        case 4:
            print('Saliendo del Cajero, hasta pronto.... ')
            salir = True
        case _:
            print('¡Opcion invalida! 😬')
