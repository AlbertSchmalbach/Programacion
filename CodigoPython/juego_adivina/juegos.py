import adivinanza
import horca


print("****************************************")
print("**********Juegos de Python*************")
print("****************************************")
print("(1) Horca (2) Adivinanza")
juego = int(input("Selecciona el juego que deseas: "))

if juego == 1:
    print('Juego de la Horca')
    horca.jugar()
elif juego == 2:
    print('Juego de adivinanza')
    adivinanza.jugar()



