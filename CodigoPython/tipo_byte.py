caracter_byte = b'Hola mundo'

# print(caracter_byte)
# print(caracter_byte[2])
# print(chr(caracter_byte[2]))
# list_caracter = caracter_byte.split()
# print(list_caracter)


# string a byte
string = 'La vida es bella'
string_codificado = string.encode('utf-8')
print(string_codificado)

# byte a string
string_decodificado = string_codificado.decode('utf-8')
print(string_decodificado)