#  Escribe un programa que se encargue de comprobar si un número es o no primo.
#  * Hecho esto, imprime los números primos entre 1 y 100.

def esPrimo(n):
    contador = 0
    for num in range(1, n+1):   
        div = n / num
        dato =  abs(div) % 1
        if dato == 0.0:
            contador += 1
    if contador == 2:
        print("Es primo")
    else:
        print("No es primo")
            

esPrimo(23)