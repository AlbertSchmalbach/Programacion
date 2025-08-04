# Escribe un programa que imprima los 50 primeros números de la sucesión
# de Fibonacci empezando en 0.
#   - La serie Fibonacci se compone por una sucesión de números en
#     la que el siguiente siempre es la suma de los dos anteriores.
#     0, 1, 1, 2, 3, 5, 8, 13...

a = 0
print(f'Valor fibonacci = {a}')
b = 1
print(f'Valor fibonacci = {b}')
for n in range(0, 10):
  c = a + b
  print(f'Valor fibonacci = {c}')
  a = b
  print(f'Valor a = {a}')
  b = c
  print(f'Valor b = {b}')