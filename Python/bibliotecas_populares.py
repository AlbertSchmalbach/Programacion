# Numpy
import numpy as np
# Crear un arreglo de números
numeros = np.array([1, 2, 3, 4, 5])
# Calcular la suma de los elementos
suma = np.sum(numeros)
# print(suma)
# Calcular el promedio de los elementos
promedio = np.mean(numeros)
# print(promedio)

# Pandas
import pandas as pd 
# Crear un DataFrame
data = {
'Nombre': ['Juan', 'María', 'Carlos'],
'Edad': [25, 30, 35],
'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
}
df = pd.DataFrame(data)
# print(df)
# Mostrar los primeros registros del DataFrame
primeros_registros = df.head()
# print(primeros_registros)
# Filtrar el DataFrame por una condición
filtro = df[df['Edad'] > 28]
# print(filtro)

# matplotlib
import matplotlib.pyplot as plt
# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
# Crear un gráfico de línea
# plt.plot(x, y)
# Mostrar el gráfico
# plt.show()

# Request
import requests
# Realizar una solicitud GET a una API
response=requests.get('https://fakestoreapi.com/products')
# Obtener los datos de la respuesta
data = response.json()
# Mostrar los datos
datos = pd.DataFrame(data)
# print(datos)