entero = int(input('Ingrese un numero entero: '))

binario = bin(entero)
hexadecimal = hex(entero)

print(f'El numero {entero} en binario es: {binario}')
print(f'El numero {entero} en hexadecimal es: {hexadecimal}')
print(f'Valor binario a entero: {int(binario, 2)}')
print(f'Valor hexadecimal a entero: {int(hexadecimal, 16)}')