print('*** Calculadora en Python ***')


salir = False

while not salir:

    print('''
Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir
''')
    opcion = int(input('Escoje una opcion: '))

    match opcion:
        case 1:
            valor1 = float(input('Dame el valor 1: '))
            valor2 = float(input('Dame el valor 2: '))
            print(f'El resultado de la suma es {valor1 + valor2}')
        case 2:
            valor1 = float(input('Dame el valor 1: '))
            valor2 = float(input('Dame el valor 2: '))
            print(f'El resultado de la resta es {valor1 - valor2}')
        case 3:
            valor1 = float(input('Dame el valor 1: '))
            valor2 = float(input('Dame el valor 2: '))
            print(f'El resultado de la multiplicacion es {valor1 * valor2}')
        case 4:
            valor1 = float(input('Dame el valor 1: '))
            valor2 = float(input('Dame el valor 2: '))
            try:
                print(f'El resultado de la Division es {valor1 / valor2}')
            except ZeroDivisionError:
                print('No se puede dividir por 0')
        case 5:
            print('Saliendo del programa de calculadora, hasta pronto.... ')
            salir = True
        case _:
            print('¡Opcion invalida! 😬')
