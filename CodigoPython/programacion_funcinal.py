# map
lista = [2, 5, 10]

cuadrado_lista = list(map(lambda x: x**2, lista))
print(cuadrado_lista)

# filter
pares_lista = list(filter(lambda x: x % 2 == 0, lista))
print(pares_lista)

# reduce
from functools import reduce
suma = reduce(lambda acc, val: acc + val, lista)
print(suma)

# Ejemplo practico
personas = [
    {'Nombre': 'Alicia', 'Edad': 22, 'Sexo': 'F'},
    {'Nombre': 'Bob', 'Edad': 25, 'Sexo': 'M'},
    {'Nombre': 'Charlie', 'Edad': 33, 'Sexo': 'M'},
    {'Nombre': 'Diana', 'Edad': 15, 'Sexo': 'F'},
    {'Nombre': 'Esteban', 'Edad': 30, 'Sexo': 'M'},
    {'Nombre': 'Federico', 'Edad': 44, 'Sexo': 'M'},
]

hombres = list(filter(lambda x: x['Sexo'] == 'M', personas))
suma_edades = reduce(lambda suma, p: suma + p['Edad'], hombres, 0)
media_edad = suma_edades/(len(hombres))
print(media_edad) 

# Operador Walrus
print(numero := input('Escribe un numero: '))

lista = []
while (entrada := input("Escribe algo: ")) != "terminar":
    lista.append(entrada)

print(lista)