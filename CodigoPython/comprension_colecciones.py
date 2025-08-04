# LISTAS COMPRIMIDAS
# [expresion for variable in lista if condicion]

# cuadrado
lista = [x ** 2 for x in range(10)]
print(f'Cuadrado de lista: {lista}')

# pares
lista2 = [x for x in range(10) if x % 2 == 0]
print(f'Numeros pares de lista2: {lista2}')

lista3 = [x ** 2 for x in range(10) if x % 2 == 0]
print(f'Cuadrado de numeros pares de lista3: {lista3}')

notas = {'Carmen':5, 'Antonio':4, 'Juan':3, 'Mónica':9, 'María': 6, 'Pablo':3}
notas_mayores = [nombre for (nombre, nota) in notas.items() if nota >= 5]
print(f'Alumnos que aprobaron: {notas_mayores}')

# DICCIONARIO COMPRIMIDOS
# {expresion-clave:expresion-valor for variables in lista if condicion}

tamano_word = {palabra:len(palabra) for palabra in ['I', 'love', 'Python']}
print(f'Tamaño palabras: {tamano_word}')

notas = {'Carmen':2, 'Antonio':4, 'Juan':3, 'Mónica':9, 'María': 6, 'Pablo':5}

alum_aprobados = {nombre: nota + 1 for (nombre, nota) in notas.items() if nota >= 5}
print(f'Alumnos aprobados: {alum_aprobados}')
