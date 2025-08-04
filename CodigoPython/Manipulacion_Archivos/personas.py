
personas = []

with open('personas.txt', 'r', encoding='utf-8') as file:
    for linea in file:
        # Dividir cada línea en los campos correspondientes
        id, nombre, apellido, nacimiento = linea.strip().split(";")


        # Crear un diccionario para cada persona
        persona = {
            "ID": id,
            "Nombre": nombre,
            "Apellido": apellido,
            "Fecha de nacimiento": nacimiento
        }

        # Añadir el diccionario a la lista
        personas.append(persona)

# Recorrer la lista y mostrar los datos de forma amigable
for persona in personas:
    print(f"ID: {persona['ID']}")
    print(f"Nombre: {persona['Nombre']}")
    print(f"Apellido: {persona['Apellido']}")
    print(f"Fecha de nacimiento: {persona['Fecha de nacimiento']}")
    print("-" * 40)




