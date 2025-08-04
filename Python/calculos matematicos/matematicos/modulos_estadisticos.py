# Modulos estadisticos

def media(*args):
    return f'El valor de la media es: {round((sum(*args)/len(*args)),2)}'


def mediana(*args):
    valores_ordenados = sorted(*args)
    indice = len(*args) // 2
    if len(*args) % 2:
        mediana = valores_ordenados[indice]
    else:
        mediana = (valores_ordenados[indice]
                   + valores_ordenados[indice + 1]) / 2

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

    
        

    
            



