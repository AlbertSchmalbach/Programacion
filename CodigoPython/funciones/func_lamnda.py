# nombre_funcion = lambda argumentos: expresion

# def num_works(text:str)-> int:
#     return len(text.split())

num_works = lambda t: len(t.split())

print(num_works('Probando funcion lamnda'))

doble = lambda x: x * 2
print(doble(5))  # Salida: 10

triplicar = lambda x: x * 3 if x > 10 else x
print(triplicar(5))  # Salida: 5
print(triplicar(15)) # Salida: 45

logic_and = lambda x, y: x & y

for i in range(2):
    for j in range(2):
        print(f'{i} & {j} = {logic_and(i, j)}')

