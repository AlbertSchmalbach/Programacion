# abs()
x = abs(-7.25)
print(x)

# all()
my_list = [True, True, True, True]
result = all(my_list)
print(result)

my_string = "Hello"
result = all(char.isalpha() for char in my_string)
print(result)  # True, ya que todos los caracteres son alfabéticos

my_list = [10, 15, 20, 25, 30]
result = all(10 <= num <= 30 for num in my_list)
print(result)  # True, ya que todos los elementos están dentro del rango [10, 30]

# any()
mylist = [False, True, False]
x = any(mylist)
print(x)

mytuple = (0, 1, False)
x = any(mytuple)
print(x)

# bin()
# Convertir el número entero 10 a su representación binaria
numero = 10
binario = bin(numero)

print(binario)  # Salida: '0b1010'

# chr()
# Obtener el carácter correspondiente al valor entero 65
char = chr(64)
print(char)  # Resultado: '@'
# Obtener caracteres especiales
special_char1 = chr(9829)  # Corazón (♥)
special_char2 = chr(9733)  # Estrella rellena (★)

print(special_char1)
print(special_char2)

# divmod()
# Obtener caracteres especiales
dividendo = 18
divisor = 3

result = divmod(dividendo, divisor)

print(f"Dividendo: {dividendo}")
print(f"Divisor: {divisor}")
print(f"Cociente: {result[0]}")
print(f"Residuo: {result[1]}")