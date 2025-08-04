from cleaner import cleaning

cleaning()

numeros = range(10)
lista_pares = [valor*valor for valor in numeros if valor % 2 == 0]
print(f'Lista de numeros pares: {lista_pares}')

# list comprehension con condicion

divisibles = [num for num in range(50) if num % 3 == 0 if num % 9 == 0]
print(f'Numeros divisibles por 3 y 9 => {divisibles}')

# pares e impares con list comprehension

lista_pares = []
lista_impares = []

[lista_pares.append(num) if num % 2 == 0 else lista_impares.append(num) for num in range(20)]

print(f'Lista de numeros Pares: {lista_pares}')
print(f'Lista de numeros Impares: {lista_impares}')

# list comprehension con multilista

lista_multiple = [[1, 2, 3], [4, 5, 6], [8, 9, 10]]
print(f'Lista multiple: {lista_multiple}')
lista_simple = [valor for sublista in lista_multiple for valor in sublista if valor % 2 == 0]
print(f'Lista simple de lista multiple: {lista_simple}')

print(5<=6)
print(4>=5)