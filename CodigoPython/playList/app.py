playlist = {}
playlist['canciones'] = []

def app():

    agregar_playlist = True
    
    while agregar_playlist:
        nombre_playlist = input('¿Como deseas nombrar la playlist?\r\n')

        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            agregar_playlist = False
            agregar_canciones()


def agregar_canciones():
    agregar_cancion = True

    while agregar_cancion:
         nombre_playlist = playlist['nombre']
         pregunta = f'\r\nAgrega canciones para la playlist {nombre_playlist}: \r\n'
         pregunta += 'Escribe "X" para dejar de agregar canciones\r\n'

         cancion = input(pregunta)

         if cancion == 'x' or cancion == 'X':
             agregar_cancion = False
             mostrar_canciones()
         else:
             playlist['canciones'].append(cancion)

def mostrar_canciones():
    nombre_playlist = playlist['nombre']
    print(f'Playlist: {nombre_playlist}\r\n')
    print('Canciones: \r\n')

    for cancion in playlist['canciones']:
        print(cancion)

app()