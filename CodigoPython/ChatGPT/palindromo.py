def es_palindromo(cadena):
    # Eliminamos espacios y convertimos a minúsculas para comparar sin distinción de mayúsculas/minúsculas
    cadena = cadena.replace(" ", "").lower()
    
    # Comparamos la cadena con su reverso
    return cadena == cadena[::-1]

# Prueba la función
cadena = input("Ingrese una cadena para verificar si es un palíndromo: ")

if es_palindromo(cadena):
    print(f"'{cadena}' es un palíndromo.")
else:
    print(f"'{cadena}' no es un palíndromo.")
