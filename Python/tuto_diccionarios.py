# definir

my_dict = dict()
my_new_dict = {}

my_dict = {
    'name': 'Albert',
    'age': 41,
    'rol': 'programer'
}

# Obtener datos
print(my_dict['name'])
print(my_dict.get('age'))

# Agregar datos
my_dict['city'] = 'Magangue'
print(my_dict)

# actualizar datos
my_dict.update({'age': 40})
print(my_dict)

# Eliminar datos
my_dict.pop('city')
print(my_dict)
my_dict.popitem()
print(my_dict)

#agregar keys y values con fromkeys
x = ('key1','key2','key3')
y = 0
my_new_dict = dict.fromkeys(x,y)
print(my_new_dict)

# Combinar diccionarios
paises = {'Colombia':'Bogota', 'Brazil':'Brasilia'}
otros_paises = {'Argentina':'Buenos Aires', 'Uruguay':'Montevideo', 'Chile':'Santiago'}

# 1 forma:
paises_union = {**paises, **otros_paises}
print(paises_union)
# 2 forma:
paises_concat = paises | otros_paises
print(paises_concat)

paises_union.update({'Bolivia':'La Paz'})
print(paises_union)

words = ('sun', 'space', 'rocket', 'earth')
words_length = {word: len(word) for word in words}
print(words_length)