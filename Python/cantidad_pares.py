def cantidad_pares(lista):
    pares = 0
    for n in lista:
        if n % 2 == 0:
            pares +=1

    return pares

lista_numeros = [2, 7, 13, 5, 8, 45, 12, 100]

print(cantidad_pares(lista_numeros))