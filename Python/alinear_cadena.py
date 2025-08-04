# CENTRAR CADENA -> center()

titulo = 'Alinear textos con Python'

# print(titulo.center(len(titulo) + 12, '*'))

# ALINEAR TEXTO A LA IZQUIERDA -> ljust()

# print(titulo.ljust(len(titulo)+12, ' '))

# ALINEAR TEXTO A LA DERECHA -> rjust()

# print(titulo.rjust(len(titulo)+12, ' '))

# MODIFICAR CADENAS

texto = ' |  Cadena de texto  | '
# print(texto)

# replace()
# print('Metodo replace =>', texto.replace(' ', ''))

# strip()
# print('Metodo strip =>',texto.strip())

# lstrip()
# print('Metodo replace =>',texto.lstrip())

# rstrip()
# print('Metodo replace =>',texto.rstrip())

# strip() con caracteres
String = '***Texto con caracteres***'

# strip(#)
# print('Metodo strip =>',String.strip('*'))

# lstrip(#)
# print('Metodo lstrip =>',String.lstrip('*'))

# rstrip(#)
# print('Metodo rstrip =>',String.rstrip('*'))

texto2 = ' *  | Hola | * '
print(texto2)
print(texto2.strip().strip('*').strip().replace(' ', ''))
