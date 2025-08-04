palabra = input('Ingrese una palabra: ').lower()

vocales = ['a', 'e', 'i', 'o', 'u']

nueva_palabra = ''

for ch in palabra:
    if ch in vocales:
        continue
    else:
        nueva_palabra += ch

print(f'La palabra sin vocales es: {nueva_palabra}')