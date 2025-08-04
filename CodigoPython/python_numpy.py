import numpy as np

# Array de una dimensión
d1 = np.array([1, 2, 3])
print(d1)

# Array de dos dimensiones
d2 = np.array([[1, 2, 3], [4, 5, 6]])
print(d2)

# Array de tres dimensiones
d3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(d3)

# Array vacio
# print(np.empty(3))

# Array de ceros
# print(np.zeros(3,2))

# Array de unos
# print(np.ones(3,2))

# Array indenty
# print(np.identity(3))

# Array arange
# print(np.arange(1, 10, 2))

# Array linspace
# print(np.linspace(0, 10, 5))

# Array random
# print(np.random.random(3,2))

# Atributos de un array

# a.ndim : Devuelve el número de dimensiones del array a.
print(d3.ndim)

# a.shape : Devuelve una tupla con las dimensiones del array a.
print(d3.shape)

# a.size : Devuelve el número de elementos del array a.
print(d3.size)

# a.dtype: Devuelve el tipo de datos de los elementos del array a.
print(d3.dtype)

# Acceso a los elementos de un array

print(d3[1, 0])
print(d3[1][0])
print(d3[:, 0:2])

# Filtrado de elementos de un array


