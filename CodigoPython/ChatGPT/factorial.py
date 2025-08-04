def calcular_factorial(numero):
    # Inicializamos el resultado como 1
    resultado = 1

    # Comprobamos si el número es negativo
    if numero < 0:
        return "El factorial no está definido para números negativos"
    # Caso especial: factorial de 0 es 1
    elif numero == 0:
        return 1
    else:
        # Calculamos el factorial
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

# Prueba la función con un número específico
numero = int(input("Ingrese un número para calcular su factorial: "))
resultado = calcular_factorial(numero)
print(f"El factorial de {numero} es {resultado}")
