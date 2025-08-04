import random

def clasificar_regalo(id: int) -> str:
    id_str = str(id)
    
    num_palindrome = lambda text: text == text[::-1]
    
    num_palindrome = num_palindrome(id_str)

    id_int = int(id_str)

    regalo = ''

    if num_palindrome and id_int % 2 != 0:
        regalo = 'girl'
    elif num_palindrome and id_int % 2 == 0:
        regalo = 'boy'
    elif id % 2 == 0 and num_palindrome == False:
        regalo = 'man'
    else:
        regalo = 'woman'
    
    return regalo

id_unico = random.randint(100, 999)



clasificar_regalo(id_unico)


