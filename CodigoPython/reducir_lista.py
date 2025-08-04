
lista = [1,2,15,7,2]

def reducir_lista(lista):
    repetidos = []
    v_alto = 0
    for v in lista:
        if v not in repetidos:
            repetidos.append(v)
    v_alto = max(repetidos)
    repetidos.remove(v_alto)
    return repetidos          
                

def promedio(lista):
    suma_v = 0
    cant_v = len(lista)
    for v in lista:
        suma_v += v
    
    return round(suma_v/cant_v,2)

lista_numeros = reducir_lista(lista)
print(promedio(lista_numeros))
