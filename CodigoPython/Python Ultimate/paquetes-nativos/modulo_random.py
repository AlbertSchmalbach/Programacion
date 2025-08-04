import random
import string
# print(random.random())
# print(random.randint(1,10))

lista = [2, 4, 6, 8, 10]
lista2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
chicas = ['Luz Saray', 'Luz karime', 'Sandra', 'Maria Fernanda', 'Misuris', 'Karolay', 'Luisana']

random.shuffle(lista)

# print(random.choice(lista2))
# print(random.choices(lista2, k=3))
# print(random.choices(chicas, k=3))

chars = string.ascii_letters
digitos = string.digits
simbolo = string.punctuation

seleccion = random.choices(chars + digitos + simbolo, k=8)
# print(seleccion)

contrasena = ''.join(seleccion)
print(contrasena)