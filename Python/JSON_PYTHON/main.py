import json

# Convertir Python a JSON (Serialización)

# Crear un diccionario Python
data = {
    "nombre": "Alberto",
    "edad": 30,
    "ciudad": "Magangue"
}

# Convertir el diccionario a una cadena JSON
json_data = json.dumps(data)

# print(json_data)

data = {
    "Country": "Colombia",
    "Departament" : "Bolivar",
    "City": "Magangue"
}

json_data = json.dumps(data, indent=3, separators=(". ", " = "), sort_keys=True)

print(json_data)

# Diccionario de Python
# print(json.dumps({"País":"España", "Comunidad":"Madrid",}))

# Lista de Python
# print(json.dumps(["Aranjuez","Las Rozas"]))

# Tupla de Python
# print(json.dumps(("Aranjuez","Las Rozas")))

# Cadena de Python
# print(json.dumps("Catalina"))

# Entero de Python
# print(json.dumps(32))

# Número decimal de Python
# print(json.dumps(32.10))

# Booleano True de Python
# print(json.dumps(True))

# Booleano False de Python
# print(json.dumps(False))

# Valor nulo de Python (None)
# print(json.dumps(None))

# Convertir JSON a Python (Deserialización)

# Cadena JSON
json_data = '{"nombre": "Luz Saray", "edad": 23, "ciudad": "Magangue"}'

# Convertir la cadena JSON a un diccionario Python
data = json.loads(json_data)

print(data)
print(data["nombre"])

# Código JSON:

x = '{ "País":"España", "Comunidad":"Madrid", "Ciudad":"Alcobendas"}'

# parse x:

y = json.loads(x)

# El resultado es un diccionario de python:

print(y["Ciudad"])

# Leer datos JSON desde un archivo de python


# Leer el contenido del archivo
with open('JSON_PYTHON/data.json', 'r') as file:
    json_data = file.read()

    # Convertir la cadena JSON a un diccionario Python
    data = json.loads(json_data)

    print(data)

# Escribir datos JSON en un archivo de python

# Datos como un diccionario Python
data = {
    "nombre": "Luz Saray",
    "edad": 23,
    "ciudad": "Magangue"
}

# Convertir el diccionario a una cadena JSON
json_data = json.dumps(data)

# Escribir la cadena JSON en un archivo
with open('JSON_PYTHON/mydata.json', 'w') as file:
    file.write(json_data)