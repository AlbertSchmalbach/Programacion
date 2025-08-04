numeros = [2, 7, 10, 15, 20]

print(*numeros)


def sumar(a, b, c, d, e):
    print(f'La suma es : {a+b+c+d+e}')
    
    
# sumar(*numeros)


x, y, *z = numeros

# print(x, y, z, end='\t')

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [lista1, lista2]

print(f'Lista de listas =>{lista3}')

lista3 = [*lista1, *lista2]

print(f'Unica lista => {lista3}')

# Con dict

dict1 = {'a':12, 'b':18, 'c': 10}
dict2 = {'d':14, 'h':12, 'i': 8}

dict3 = {**dict1, **dict2}

print(f'Diccionario => {dict3}' )
