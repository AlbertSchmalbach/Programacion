# -*- coding: utf-8 -*-
"""
Created on Thu May 25 21:36:46 2023

@author: KHAdmin
"""
#PROGRAMACION FUNCIONAL

from functools import reduce

#funcion que recibe una funcion como parametro
def aplica(funcion, argumento):
    return funcion(argumento)

def cuadrado(n):
    return n*n

def cubo(n):
    return n**3

print(f'El cuadrado es: {aplica(cuadrado, 5)}')
print(f'El cubo es: {aplica(cubo, 5)}')

#Funciones anónimas (lambda)
area = lambda base, altura : base * altura
print(f'El area es: {area(4, 5)}')

#Aplicar una función a todos los elementos de una colección iterable (map)
cuadrado = lambda n: n * n

iter1 = list(map(cuadrado, [1, 2, 3]))

print(iter1)

rectangulo = lambda a, b : a * b

iter2 = tuple(map(rectangulo, (1, 2, 3), (4, 5, 6)))
print(iter2)

#Filtrar los elementos de una colección iterable (filter)
par = lambda n : n % 2 == 0

iter_par = list(filter(par, range(10)))
print(iter_par)

#Combinar los elementos de varias colecciones iterables (zip)
asignaturas = ['Matemáticas', 'Física', 'Química', 'Economía']
notas = [6.0, 3.5, 7.5, 8.0]

nota_final = list(zip(asignaturas, notas))
nota_final = dict(zip(asignaturas, notas))
print(nota_final)

#Operar todos los elementos de una colección iterable (reduce)
producto = lambda n, m : n * m

reducido = reduce(producto, range(1, 5))
print(f'El resultado de aplicar reduce(): {reducido}')
