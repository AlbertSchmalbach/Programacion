def palindromo(sentence):
    """_summary_

    Args:
        sentence (String): Palabra o frase cualquiera

    Returns:
        bool: Retorna True si es un palindromo, False si no lo es

    Examples:
    >>> palindromo('Oso')
    True

    >>> palindromo('Lobo')
    False

    >>> palindromo('Anita lava la tina')
    True

    """
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]

# print(palindromo('Oso'))
# print(palindromo('Lobo'))
# print(palindromo('Anita lava la tina'))

# print(palindromo.__doc__)