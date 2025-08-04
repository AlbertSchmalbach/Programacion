# Realiza una función llamada relacion(a, b) que a partir de dos números cumpla lo siguiente:

# Si el primer número es mayor que el segundo, debe devolver 1.
# Si el primer número es menor que el segundo, debe devolver -1.
# Si ambos números son iguales, debe devolver un 0.
# Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'.

def relacion(a, b):
    resultado = 0
    if a > b:
        resultado = 1
    elif a < b:
        resultado = -1
    else:
        resultado = 0

    return resultado

# Realiza una función llamada intermedio(a, b) que a partir de dos números, devuelva su punto intermedio. Cuando lo tengas comprueba el punto intermedio entre -12 y 24:

def intermedio(a, b):
    punto_medio = (a + b)/2
    return punto_medio

# Realiza una función llamada recortar(numero, minimo, maximo) que reciba tres parámetros. El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:

# Devolver el límite inferior si el número es menor que éste
# Devolver el límite superior si el número es mayor que éste.
# Devolver el número sin cambios si no se supera ningún límite.
# Comprueba el resultado de recortar 15 entre los límites 0 y 10.

def recortar(numero, minimo, maximo):

    resultado = 0
    if numero < minimo:
        resultado = minimo
    elif numero > maximo:
        resultado = maximo
    else:
        resultado = numero
    return resultado

# Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.

def separar(lista):
    pares = []
    impares = []
    for n in lista:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)  
    pares.sort()
    impares.sort()
    return pares, impares

lista = [6,5,2,1,7]
pares, impares = separar(lista) 
print(pares)
print(impares)