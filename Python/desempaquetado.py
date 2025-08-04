# Desempaquetando tuplas

edades = 15, 22, 17, 13, 28, 35

edad1, _, edad3, _, edad5, _ = edades
edad1, _, edad3, *_ = edades

# print(edad1)
# print(edad3)
print(_)

# Desempaquetando listas

num1, num2, num3 = [15, 27, 90]

print(num1)
print(num2)
print(num3)

# Desempaquetando  funciones

def desempaca_funcion():
    return 1, 2, 3

n1, n2, n3 = desempaca_funcion()

print(n1)
print(n2)
print(n3)

# Ejemplo desempacado

tiempo = '17:25'
hora, _ , minuto = tiempo.partition(':')
print('Hora: ', hora)
print('Minuto: ', minuto)