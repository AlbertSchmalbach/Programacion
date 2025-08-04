diccionario = {'nombre': 'Alberto', 'apellido': 'Schmalbach', 'edad': 40}

# print(diccionario['nombre'])

diccionario['email'] = 'beto21048@gmail.com'

print(diccionario.get('edads', 'Llave no encontrada'))

print(diccionario.setdefault('color', 'Color no existe'))

print(diccionario)