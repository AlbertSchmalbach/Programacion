# Modulos estadisticos

def media(*args):
    return f'El valor de la media es: {round((sum(*args)/len(*args)),2)}'

def mediana(*args):
    datos_ordenados = sorted(*args)
    tamano = len(datos_ordenados)
    indice_medio = tamano // 2

    mediana = 0

    if tamano % 2 == 0:
        suma_indices = datos_ordenados[indice_medio-1] + datos_ordenados[indice_medio]
        mediana = int(suma_indices/2)
    else:
        mediana = datos_ordenados[indice_medio]

    return f'El valor de la mediana es: {mediana}'

def moda(*args):
    # Creo un conjunto con los datos unicos
    numeros = set(*args)
    # Creo un diccionario
    diccionario = {}

    # Recorro el conjunto
    for n in numeros:
        # Guardo la cantidad en que aparece de cada numero del conjunto
        v = list(*args).count(n)
        # Añado el valor al numero correspondiente en el diccionario
        diccionario[n] = v

    # Guardo las cantidades de cada numero en una lista
    max_numeros = []   
    for v in diccionario.values():
        max_numeros.append(v)

    # valor mas alto de la lista
    valor_alto = max(max_numeros)

    nums_modas = []
    # Recorro el diccionario y busco la llave del valor mas alto
    for key, value in diccionario.items():
        if valor_alto == value:
            nums_modas.append(key)
            

    return f'El valor de la moda es: {" ".join([str(_) for _ in nums_modas])}'


if __name__ == '__main__':
    datos = [81, 89, 92, 85, 93, 62, 85, 105, 90]
    print(media(datos))  
    print(mediana(datos))
    print(moda(datos))

    
        

    
            



