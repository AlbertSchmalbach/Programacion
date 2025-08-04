import random

def lanzar_dados():
    num1 = random.choice(list(range(1,6+1)))
    num2 = random.choice(list(range(1,6+1)))
    
    return num1, num2


def evaluar_jugada(v1, v2):
    suma_dados = v1 + v2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


dado1, dado2 = lanzar_dados()
print(evaluar_jugada(dado1,dado2))