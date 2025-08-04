def todos_positivos(lista_numeros):
    positivos = []
    negativos = []
    for n in lista_numeros:
        if n >= 0:
            positivos.append(n)
        else:
            negativos.append(n)
    
    if positivos and len(negativos) == 0:
        return True
    else:
        return False


lista_numeros = [5, -1, 8]

print(todos_positivos(lista_numeros))