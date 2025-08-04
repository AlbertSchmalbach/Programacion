import cleaner as cl

cl.cleaning()

mezcla = [(1,'a'), (2,'b'), (3,'c')]

numeros, letras = zip(*mezcla)

print(f'Numeros: {numeros} Letras: {letras}')