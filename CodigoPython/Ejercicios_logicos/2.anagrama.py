# Escribe una función que reciba dos palabras (String) y retorne
# verdadero o falso (Bool) según sean o no anagramas.
# Un Anagrama consiste en formar una palabra reordenando TODAS
# las letras de otra palabra inicial.
# NO hace falta comprobar que ambas palabras existan.
# Dos palabras exactamente iguales no son anagrama.

def anagrama(word1, word2):
    letterEqual = ''
    for letter in word1.lower():
        if letter in word2.lower():
            letterEqual += letter
            if len(letterEqual)==len(word1) and len(letterEqual) == len(word2):
                return True
    return False


print(anagrama('Tinieblas', 'Sibilante'))