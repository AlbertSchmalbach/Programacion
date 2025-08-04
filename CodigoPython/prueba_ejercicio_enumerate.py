lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in list(enumerate(lista_nombres)):
    if nombre[0]== 'M':
        print(indice)
