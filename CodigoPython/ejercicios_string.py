from pprint import pprint

# 1. Eliminar los espacios en blanco de un string

def cadena_sin_espacio(cadena):
    cadena = [char for char in cadena if char != " "]
    cadena = ''.join(cadena)
    return cadena

# 2. Contar en un diccionario cuanto se repiten los caracteres de un string

def contar_caracteres(cadena):
    cadena = cadena.replace(' ', '').lower()

    caracteres = dict()

    for char in cadena:
        if char in caracteres:
            caracteres[char] += 1
        else:
            caracteres[char] = 1

    return caracteres

def ordena_dict(dict):
    return sorted(dict.items(), key = lambda key: key[1], reverse=True)

def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta

def crea_mensaje(diccionario):
    mensaje = "Los que mas se repiten son: \n"
    for k, v in diccionario.items():
        mensaje += f"- {k} con valor {v} repeticiones \n"
    
    return mensaje

sin_espacio = cadena_sin_espacio('Luz Saray')
contar_char = contar_caracteres(sin_espacio)
# pprint(contar_char, width=2)
ordenados = ordena_dict(contar_char)
mayor = mayores_tuplas(ordenados)
mensaje = crea_mensaje(mayor)
print(mensaje)
        

        







