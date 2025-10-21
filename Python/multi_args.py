def sum_resgister(*args):
    contador = 0
    for r in args:
        contador += 1

    return contador


res = sum_resgister("Hola", "Mundo", "que", "tal", "como", "amanecieron")

print(res)
