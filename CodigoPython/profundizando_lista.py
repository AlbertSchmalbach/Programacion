name1 = ['Juan', 'Carla', 'Pedro']
name2 = 'Laura Maria Paola Melany Said'.split()

# print(f'Suma lista: {name1 + name2}')
# name1.extend(name2)
# print('Lista extendida: ', name1)

# lista de numero
numero = [15, 84, 50, 12, 8, 10, 2, 5, 7, 16]

# print('Indice de 8: ', numero.index(8))

# numero.sort()
# print(f'Lista ordenada: {numero}')

# numero.reverse()
# print(f'Lista invertida (Desc): {numero}')

# numero.sort(reverse=True)
# print(f'Lista invertida (Asc): {numero}')

# Copiar listas
numero2 = numero
# print(f'Es la misma lista? {numero is numero2}')

numero2 = numero.copy()
# print(f'Es la misma lista? {numero is numero2}')

numero2 = numero[:]
# print(f'Es la misma lista? {numero is numero2}')

# build-in function

numeros = [[2, 6, 7], [12, 3, 37, 10], [7, 40, 14, 1], [2, 7], [5, 61, 8, 11]]

numeros.sort(key=len)
print(numeros)

names = ['Alberto', 'Raul', 'Natalia', 'Yulis', 'Catalina']
names = sorted(names)
print(names)

names = sorted(names, reverse=True)
print(names)

