from operaciones.aritmetica import suma, division, potencia

num1 = int(input('Ingresa un numero: '))
num2 = int(input('Ingresa otro numero: '))

result_suma = suma(num1, num2)
result_div = division(num1, num2)
result_pot = potencia(num1, num2)

print(f"Resultado de la suma: {result_suma}")
print(f"Resultado de la division: {result_div}")