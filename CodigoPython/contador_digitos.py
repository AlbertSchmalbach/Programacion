number = int(input('Ingrese una cifra: '))
counter = 0
cifra = number

while number > 0:
    number = number // 10
    counter += 1

print(f'La cifra {cifra} tiene {counter} digitos')
