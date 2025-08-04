# Mi Codigo

# print('Bienvenidos a la calculadora')
# print('Para salir escribe exit')
# print('Las operaciones son suma, resta, multiplicacion y division')

# numero = input('Ingresa un numero: ')

# if numero.isdigit():
#     numero = int(numero)
#     while numero:
#         operacion = input('Ingresa una operacion: ')
#         if operacion == str.lower('exit'):
#             break
#         else:
#             if operacion == 'suma':
#                 numero2 = int(input('Ingresa un siguiente numero: '))
#                 numero+= numero2
#                 print('El resultado es: ', numero)
#             elif operacion == 'resta':
#                 numero2 = int(input('Ingresa un siguiente numero: '))
#                 numero-= numero2
#                 print('El resultado es: ', numero)
#             elif operacion == 'multiplicacion':
#                 numero2 = int(input('Ingresa un siguiente numero: '))
#                 numero*= numero2
#                 print('El resultado es: ', numero)
#             elif operacion == 'division':
#                 numero2 = int(input('Ingresa un siguiente numero: '))
#                 numero-= numero2
#                 print('El resultado es: ', numero)
# else:
#     print('El dato ingresado no es numero')
#     print('Ejecuta el programa nuevamente')


# Con ChatGPT
    
print('Bienvenidos a la calculadora')
print('Para salir escribe exit')
print('Las operaciones son suma, resta, multiplicacion y division')

def validar_numero(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False

numero = input('Ingresa un número: ')

if numero.lower() == 'exit':
    print('¡Hasta luego!')
else:
    if validar_numero(numero):
        numero = float(numero)
        while True:
            operacion = input('Ingresa una operación: ')
            if operacion.lower() == 'exit':
                print('¡Hasta luego!')
                break
            elif operacion in ['suma', 'resta', 'multiplicacion', 'division']:
                numero2 = input('Ingresa el siguiente número: ')
                if not validar_numero(numero2):
                    print('El dato ingresado no es número. Intenta nuevamente.')
                    continue
                
                numero2 = float(numero2)
                
                if operacion == 'suma':
                    numero += numero2
                elif operacion == 'resta':
                    numero -= numero2
                elif operacion == 'multiplicacion':
                    numero *= numero2
                elif operacion == 'division':
                    if numero2 != 0:
                        numero /= numero2
                    else:
                        print('Error: División por cero.')
                        continue
                
                print('El resultado es:', numero)
            else:
                print('Operación inválida. Las operaciones válidas son: suma, resta, multiplicacion, division')
    else:
        print('El dato ingresado no es número')
        print('Ejecuta el programa nuevamente')

    


