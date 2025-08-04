# Asignacion mulitple

# Listas
edades = [24, 40, 32]
edad1, edad2, edad3 = edades
print('Asignacion Multiple Listas')
print(edad1)
print(edad2)
print(edad3)
print()
# Conjuntos
frutas = {'Pera', 'Manzana', 'Uva'}
f1, f2, f3 = frutas
print('Asignacion Multiple Sets')
print(f1)
print(f2)
print(f3)
print()
# Tuplas
nombres = ('Ana', 'Misuris', 'Yulianis')
name1, name2, name3 = nombres
print('Asignacion Multiple Tuplas')
print(name1)
print(name2)
print(name3)
print()
# Asignaciones con Dict

user = {
    'name': 'Alberto',
    'age': 35
}

# llaves
name, age = user
print('Asignacion Multiple Dict(key)')
print(name)
print(age)
print()
# Valores
name, age = user.values()
print('Asignacion Multiple Dict(values)')
print(name)
print(age)
print()

# Asignaciones con funciones y métodos
def get_profile():
    username = 'Albert'
    email = 'alber@cosasdedevs.com'
    photo = '../files/photo.png'

    return username, email, photo

username, email, photo = get_profile()
print(username)

# Asignaciones con el operador *

# Caso 1
number_list1 = [4, 3, 0, 1, 5]
x, *y, z = number_list1
print('Asignacion Multiple Operador * 1')
print(x)
print(y)
print(z)
print()
# Caso 2
number_list2 = [4, 3, 0, 1, 5]
*x, y, z = number_list2
print('Asignacion Multiple Operador * 2')
print(x)
print(y)
print(z)
print()
# Caso 3
number_list3 = [4, 3, 0, 1, 5]
x, y, *z = number_list3
print('Asignacion Multiple Operador * 2')
print(x)
print(y)
print(z)