# Modulos matematicos

def suma(*args):
    return sum(args)

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print('No se puede dividir por Cero')