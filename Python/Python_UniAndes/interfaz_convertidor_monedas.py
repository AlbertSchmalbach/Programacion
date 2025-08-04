import convertidor_moneda as cm
import cleaner as cl

cl.cleaning()

def ejecutar_convertir_a_dolares() -> None:
    pesos = float(input('Ingrese la cantidad de pesos: '))
    trm = float(input('Ingrese la TRM: '))
    dolares = cm.convertir_a_dolares(pesos, trm)
    print(f'{pesos} pesos son, {round(dolares, 2)} dolares')

def ejecutar_convertir_a_pesos() -> None:
    dolares = float(input('Ingrese la cantidad de dolares: '))
    trm = float(input('Ingrese la TRM: '))
    pesos = cm.convertir_a_pesos(dolares, trm)
    print(f'{dolares} dolares son, {round(pesos, )} pesos')

def mostrar_menu() -> str:
    menu = """
    Seleccione una opcion:
    1. Convertir de dolares a pesos
    2. Convertir de pesos a dolares
    3. Salir

    Opcion seleccionada: """
    opcion = input(menu)
    return opcion

def iniciar_aplicacion() -> None:
    continuar = True
    while continuar:
        opcion = mostrar_menu()
        if opcion == '1':
            cl.cleaning()
            ejecutar_convertir_a_dolares()
        elif opcion == '2':
            cl.cleaning()
            ejecutar_convertir_a_pesos()
        elif opcion == '3':
            cl.cleaning()
            continuar = False
        else:
            print('La opcion seleccionada no es valida')
    
iniciar_aplicacion()
