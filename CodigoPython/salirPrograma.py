import sys

while True:
    print('Escribe exit para salir.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('Escribiste ' + response + '.')