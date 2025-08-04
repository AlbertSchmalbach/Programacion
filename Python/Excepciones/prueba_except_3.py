import math

def sacaRaizCuadrada(num):

    if num < 0:
        raise ValueError("No se admiten numeros negativos")
    else:
        return math.sqrt(num)
    
num = int(input('Ingresa un numero: '))

try:
    print(sacaRaizCuadrada(num))
except ValueError as errorValorNegativo:
    print(f"Error => {errorValorNegativo}")
finally:
    print("Programa ejecutado")

