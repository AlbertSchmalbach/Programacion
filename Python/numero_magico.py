from random import randint

numberUser = int(input('Ingrese un numero: '))
numberMagic = randint(1, 20)

while numberMagic != numberUser:
    if numberUser < numberMagic:
        print('El numero es mayor')
    else:
        print('El numero es menor')
             
    # Solicitar un nuevo número al usuario
    numberUser = int(input('Intenta nuevamente: '))       
else:
   print('¡Felicidades!... has adivinado el numero 👍')