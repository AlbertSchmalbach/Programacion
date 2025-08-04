print('*****Calculadora en Python con Funciones*****')

# Definimos la funcion de mostrar menu
def mostrar_menu():
    print('''
 Operaciones que puedes realizar:
        1. Suma
        2. Resta
        3. Multiplicacion
        4. Division
        5. Salir 
''') 
    opcion = int(input('Escoge una opcion: '))
    return opcion

# Definimos la funcion para solicitar los valores
def pedir_valores():
    valor1 = int(input('Ingrese el primer valor: '))
    valor2 = int(input('Ingrese el segundo valor: '))

    return valor1, valor2

# Definimos la funcion para ejecutar la operacion solicitada
def ejecutar_operacion(opcion, salir):
    resultado = 0
    # a, b = pedir_valores()
    match opcion:
        case 1:
            print('*** Suma ***')
            a, b = pedir_valores()
            resultado = a + b
            print(f'El resultado de la suma es: {resultado}')
        case 2:
            print('*** Resta ***')
            a, b = pedir_valores()
            resultado = a - b
            print(f'El resultado de la resta es: {resultado}')
        case 3:
            print('*** Multiplicacion ***')
            a, b = pedir_valores()
            resultado = a * b
            print(f'El resultado de la multiplicacion es: {resultado}')
        case 4:
            print('*** Division ***')
            a, b = pedir_valores()
            resultado = a / b
            print(f'El resultado de la division es: {resultado}')
        case 5:
            print('Saliendo de la calculadora. Hasta pronto...')
            salir = True
        case _:
            print('Operacion invalida')
    return salir
        
# Codigo principal
salir = False
while not salir:
    opcion = mostrar_menu()
    salir = ejecutar_operacion(opcion, salir)
    

