def generador():
    for n in range(0, 20, 2):
        yield n


pares = generador()

for par in pares:
    print(par)