import cleaner as cl

cl.cleaning()

a, b = 'hola', 'adios'

print(a, b)

# swap (intercambio)

a, b = b, a

print(a, b)

# Regresar multiples valores

def minmax(lista):
    return min(lista), max(lista)

min, max = minmax([12, 45, 26, 18, 3])

print(f'Valor min: {min} Valor max: {max}')

def sumar(*args):
    return sum(args)


sumando = sumar(12, 80, 2, 18)

print(sumando)