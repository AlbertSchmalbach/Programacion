def not_space(string):
    text_not_space = ""
    for char in string:
        if char != " ":
            text_not_space += char
    return text_not_space


def text_reverse(string):
    texto_reverse = ""
    for char in string:
        texto_reverse = char + texto_reverse
    return texto_reverse



def es_pailindromo(texto:str) -> bool:
    texto = not_space(texto).lower()
    texto_reverse = text_reverse(texto)
    
    return texto == texto_reverse
    
    
print("Abba", es_pailindromo("Abba"))
print("Reconocer", es_pailindromo("Reconocer"))
print("Amo la paloma", es_pailindromo("Amo la paloma"))
print("Hola mundo", es_pailindromo("Hola mundo"))
