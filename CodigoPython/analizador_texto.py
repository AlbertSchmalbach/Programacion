def analizador_text(texto, letras):
    texto = texto.lower()

    letras.append(input('Ingresa la primera letra: ').lower())
    letras.append(input('Ingresa la segunda letra: ').lower())
    letras.append(input('Ingresa la tercera letra: ').lower())

    print("\n")
    print("CANTIDAD DE LETRAS")
    cant_letras1 = texto.count(letras[0])
    cant_letras2 = texto.count(letras[1])
    cant_letras3 = texto.count(letras[2])

    print(f"Hemos encontrado la letra '{letras[0]}' unas {cant_letras1} veces")
    print(f"Hemos encontrado la letra '{letras[1]}' unas {cant_letras2} veces")
    print(f"Hemos encontrado la letra '{letras[2]}' unas {cant_letras3} veces")

    print("\n")
    print("CANTIDAD DE PALABRAS")
    palabras = texto.split()
    print(f"Hemos encontrado {len(palabras)} palabras en tu texto")

    print("\n")
    print("LETRAS DE INICIO Y FIN")
    letra_inicio = texto[0]
    letra_fin = texto[-1]
    print(f"La letra inicial es '{letra_inicio}' y la final es '{letra_fin}'")

    print("\n")
    print("TEXTO INVERTIDO")
    palabras.reverse()
    texto_invertido = ' '.join(palabras)
    print(texto_invertido)

    print("\n")
    print("PALABRA 'PYTHON' EN TEXTO")
    buscar_python = "python" in texto
    dic = {True:"si", False:"no"}
    print(f"La palabra 'python' {dic[buscar_python]} se encuentra en el texto")

texto = input('Ingresa un texto: ')
letras = []

analizador_text(texto, letras)

