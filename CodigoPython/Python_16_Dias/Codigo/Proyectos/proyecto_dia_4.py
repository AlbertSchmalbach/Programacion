import random

numero_maquina = random.randint(1, 100+1)
print(numero_maquina)
nombre_usuario = input("Nombre de usuario: ")
numero_usuario = int(input(f"Bueno {nombre_usuario}, he pensado un numero entre 1 y 100, y tienes solo 8 intentos para adivinar, ¿cual crees que es? " ))

cant_intentos = 8
numero_intentos = 1

while cant_intentos >numero_intentos:
    
    if numero_usuario < numero_maquina:
        print("Su respuesta es incorrecta. ha elegido un número menor al número secreto")
        numero_usuario = int(input("Elija otro numero: " ))
    elif numero_usuario > numero_maquina:
        print("Su respuesta es incorrecta. ha elegido un número mayor al número secreto")
        numero_usuario = int(input("Elija otro numero: " ))
    elif numero_usuario == numero_maquina:    
        print(f"Felicitaciones {nombre_usuario}!!!...Has ganado en el intento numero {numero_intentos} 🎉🥇🏆")
        break
    else:
    
        print("Ha elegido un número que no está permitido")
    
    numero_intentos +=1

print("Juego finalizado")