import random, sys

print('PIEDRA, PAPEL, TIJERA')

# Estas variables mantienen un registro del número de victorias, derrotas y empates.
victorias = 0
derrotas = 0
empates = 0

while True: # El bucle principal del juego.
    print('%s Victorias, %s Derrotas, %s Empates' % (victorias, derrotas, empates))
    while True: # El bucle de entrada del jugador.
        print('Ingrese su movimiento: (r)ock (p)aper (s)cissors o (q)uit')
        movimientoJugador = input()
        if movimientoJugador == 'q':
            sys.exit() # Salir del programa.
        if movimientoJugador == 'r' or movimientoJugador == 'p' or movimientoJugador == 's':
            break # Salir del bucle de entrada del jugador.
        print('Escribe uno de r, p, s o q.')

    # Muestra lo que eligió el jugador:
    if movimientoJugador == 'r':
        print('PIEDRA versus...')
    elif movimientoJugador == 'p':
        print('PAPEL versus...')
    elif movimientoJugador == 's':
        print('TIJERAS versus...')

    # Muestra lo que eligió la computadora:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('PIEDRA')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPEL')
    elif randomNumber == 3:
        computerMove = 's'
        print('TIJERAS')

    # Muestra y registra la victoria/derrota/empate:
    if movimientoJugador == computerMove:
        print('¡Es un empate!')
        ties = ties + 1
    elif movimientoJugador == 'r' and computerMove == 's':
        print('¡Ganaste!')
        gana = gana + 1
    elif movimientoJugador == 'p' and computerMove == 'r':
        print('¡Ganaste!')
        victorias = victorias + 1
    elif movimientoJugador == 's' and computerMove == 'p':
        print('¡Ganaste!')
        victorias = victorias + 1
    elif movimientoJugador == 'r' and computerMove == 'p':
        print('¡Pierdes!')
        derrotas = derrotas + 1
    elif movimientoJugador == 'p' and computerMove == 's':
        print('¡Pierdes!')
        derrotas = derrotas + 1
    elif movimientoJugador == 's' and computerMove == 'r':
        print('¡Pierdes!')
        derrotas = derrotas + 1