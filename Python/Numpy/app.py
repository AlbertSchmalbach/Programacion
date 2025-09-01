import numpy as np
import time

# ndarray
# x = np.array([1, 2, 3, 4, 5])
# print(type(x))
# print(x)

# Dimesion array
# print(x.ndim)
# Tamaño del array
# print(x.size)
# Forma
# print(x.shape)
# Tipo de datos array
# print(x.dtype)

# Datos heterogéneos
# y = np.array([4, 'Einstein', 1e-7])
# print(y)

# Tipos de datos
# a = np.array(range(5), dtype='int32')
# print(a.dtype)
# b = a.astype('float')
# print(b.dtype)

# array vs list
inicio = time.time()
array_list = list(range(10_000_000))
fin = time.time()
tiempo_eje = fin-inicio

print(f"El codigo 1 tardo {tiempo_eje:.2f} segundos en ejecutarse.")


inicio = time.time()
array_ndarray = np.array(array_list)
fin = time.time()
tiempo_eje = fin-inicio

print(f"El codigo 2 tardo {tiempo_eje:.2f} segundos en ejecutarse.")

# Matrices
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(M)
print()

# Ejercicios

m1 = np.array([[88, 23, 39, 41]])

m2 = np.array([[76.4, 21.7, 28.4], [41.2, 52.8, 68.9]])

m3 = np.array([[12], [4], [9], [8]])

m4 = np.array(range(1,13)).reshape(3, 4) # cambiar su forma mediante la función np.reshape()

# print(m1)
# print()
# print(m2)
# print()
# print(m3)
# print()
# print(m4)

# Persistiendo arrays

# 1 forma
np.save('mi_matriz', M)
# 2 forma
np.savetxt('Mi_Matriz.csv', M)

# Cargar datos devuelta en narray
M_reloaded = np.loadtxt('Mi_Matriz.csv')

print(M_reloaded)
