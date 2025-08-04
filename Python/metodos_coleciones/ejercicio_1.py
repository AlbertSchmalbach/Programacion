# Utilizando todo lo que sabes sobre cadenas, listas, sus métodos internos... Transforma este texto:

cadena = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

# Resultado =>
# Un día que el viento soplaba con fuerza...
# - Mira como se mueve aquella banderola -dijo un monje.
# - Lo que se mueve es el viento -respondió otro monje.
# - Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.


cadena = cadena.split('#')
print(f'{cadena[0].capitalize()}...')
for linea in cadena[1:]:
    print(f'- {linea.capitalize()}')
    