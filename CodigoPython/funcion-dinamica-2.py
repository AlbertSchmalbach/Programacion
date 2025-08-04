def suma_menores(lista_numeros):
    suma_numeros = 0
    for num in lista_numeros:
        if num in range(0, 1000):
            suma_numeros += num
            
    return suma_numeros
    
lista_numeros = [-5, 8, 12]

print(suma_menores(lista_numeros))