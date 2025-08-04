import random

aleatorio = random.randint(1,10)

numero_user = int(input("Adivina el numero: "))

if numero_user == aleatorio:
    print("Felicidades adivinaste el numero")
else:
    print("No adivinaste el numero")