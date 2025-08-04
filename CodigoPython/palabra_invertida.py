def invertir_palabra(palabra:str):
    palabra_invertida = []
    for chr in palabra:
        palabra_invertida.insert(0, chr)

    palabra = "".join(palabra_invertida).upper()
    return palabra
    

print(invertir_palabra("Amor"))