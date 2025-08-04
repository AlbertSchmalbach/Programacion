# def palindromo(text):
#     texto = text.replace(' ', '').lower()
#     print('Es un palíndromo') if texto == texto[::-1] else print('No es un palíndromo')

def palindromo(string):
    string = string.replace(' ','').lower()
    startStr = 0
    endStr = len(string) - 1  

    for s in string:
        if string[startStr] != string[endStr]:
            return False
    return True    
    
# palindromo('Ten animals I slam in a net')

print(palindromo('opano'))