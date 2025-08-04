def suma(a:int,b:int)-> int:
    return a + b

def resta(a:int,b:int)-> int:
    return a - b

def multiplicacion(a:int,b:int)-> int:
    return a * b

def division(a:int,b:int)-> int:
    if not b == 0:
        return a // b
    else:
        print("No se puede realizar division por 0")
        return "error"

def potencia(a:int,b:int)-> int:
    return a**b