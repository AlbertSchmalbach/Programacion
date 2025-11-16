"""Typing con Python"""

var = 42

print(f'Variable {var} del tipo : {type(var)}')

# var: tipo = valor

myVar: int = 25

user_id: int | None = None

print(f'Variable {myVar} del tipo : {type(myVar)}')

def suma(a: int, b: int) -> int:
    return a + b

res = suma(10, 25)
print(res)

articles: list = [{'title':'example'}]

articles.append({'author':'Pipe pombo'})

print(articles)