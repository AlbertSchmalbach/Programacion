cadena1 = set(input('Palabra a buscar: '))
cadena2 = set(input('Esta la palabra en?: '))

intersec = cadena1 & cadena2

if intersec and (len(cadena1)==len(intersec)):
    print('si')
else:
    print('no')
    

