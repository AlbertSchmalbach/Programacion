import random

lista_numero = [2, 5, 8, 12, 30]

def lanzar_moneda():
    valor = ["Cara", "Cruz"]
    return random.choice(valor)


def probar_suerte(lado_moneda, lista):
    if lado_moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
        return lista
    

lado_moneda = lanzar_moneda()
# print(lado_moneda)
print(probar_suerte(lado_moneda, lista_numero))