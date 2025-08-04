from urllib import request
import json

# obtener respuesta de la url
res = request.urlopen('https://jsonplaceholder.typicode.com/todos/')
# print('RESPONSE:', res)

# Cuerpo de la respuesta
body_res = res.read()
# print(body_res)

# Procesamos la respuesta
json_res = json.loads(body_res.decode('utf-8'))
# print(json_res)

# Imprimir solo los titulos
for book in json_res:
    print(f'{book["id"]}. {book["title"]}')