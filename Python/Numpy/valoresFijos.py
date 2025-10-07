import numpy as np

# Array de Ceros fijos
nArrayceros = np.zeros((3, 4))
# print(nArrayceros)

# Valores espaciados
n = np.arange(21)
# print(n)
m = np.arange(10, 20)
# print(m)

# Valores flotantes espaciados
x = np.linspace(10, 20)
# print(x)

# aleatorios

# enteros
aleatorio1 = np.random.randint(1, 10, size=4)
# print(aleatorio1)
# flotantes
aleatorio2 = np.random.random(10)
# print(aleatorio2)
aleatorio3 = np.random.uniform(1, 100, size=3)
# print(aleatorio3)

dist = np.random.normal(0, 5, size=1_000_000)

# print(dist)
# print(dist[:20])
# print(dist.mean())
# print(dist.std())

coins = np.random.choice(['Misuris Paola', 'Luz Saray'], size=20)

print('Luz Saray: ', sum(coins == 'Luz Saray'))
print('Misuris: ', sum(coins == 'Misuris Paola'))