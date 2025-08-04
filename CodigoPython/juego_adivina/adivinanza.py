import random
def jugar():
  
    print("****************************************")
    print("**********Adivina el Número*************")
    print("****************************************")
    print("*****Elige el nivel de dificultad*******")
    print("(1) Novato (2) Intermedio (3) Avanzado")

    nivel = int(input('Nivel: '))

    if nivel == 1:
        total_intentos = 20
    elif nivel == 2:
        total_intentos = 10
    else:
        total_intentos = 5

    numero_secreto = random.randint(1, 100)
    print(numero_secreto)
    puntos = 1000

    for intento in range(1, total_intentos + 1):
        print("Intento {} de {}".format(intento, total_intentos))
        entrada_str = input("Digita un número mayor que 0 y menor o igual a 100: ")
        entrada = int(entrada_str)

        if (entrada < 1 or entrada > 100):
            print("¡Debes ingresar un número entre 1 y 100!")
            continue
        
        print("El número que digitaste: ", entrada)

        acerto = numero_secreto == entrada
        mayor = entrada > numero_secreto
        menor = entrada < numero_secreto

        if (acerto):
            print(f"Has acertado el número! Tu puntaje es {puntos} 😎")
            break
        else:
            if (mayor):
                print("El número no corresponde! El número que ingresaste es mayor.")
            elif (menor):
                print("El número no corresponde! El número que ingresaste es menor.")
            puntos_perdidos = abs(numero_secreto - entrada)
            puntos = puntos - puntos_perdidos
    

    print("El juego ha concluído!")

if __name__ == '__main__':
    jugar()