colores = { "amarillo":"yellow", "azul":"blue", "verde":"green" }

print(colores.get('negro','no se encuentra'))
print(colores.keys())
print(colores.values())
print(colores.items())

for k, v in colores.items():
    print(k, v)

print(colores.pop('amarillo', 'no se ha encontrado'))
colores.clear()
print(colores)