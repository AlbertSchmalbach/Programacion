import requests
from bs4 import BeautifulSoup
import csv

# URL de la página web a analizar
url = "https://www.jw.org/es/"

# Realizar una solicitud HTTP para obtener el contenido de la página
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Analizar el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # En este ejemplo, supongamos que estamos buscando títulos y enlaces
    titulos = soup.find_all("h2")  # Cambia esto según la estructura de la página
    enlaces = soup.find_all("a")   # Cambia esto según la estructura de la página
    
    # Crear una lista para almacenar los datos
    datos = []

    # Iterar sobre los elementos y extraer información
    for titulo, enlace in zip(titulos, enlaces):
        titulo_texto = titulo.text
        enlace_href = enlace.get("href")
        
        # Agregar los datos a la lista
        datos.append([titulo_texto, enlace_href])

    # Guardar los datos en un archivo CSV
    with open("datos.csv", "w", newline="") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        
        # Escribir encabezados
        escritor_csv.writerow(["Título", "Enlace"])
        
        # Escribir los datos
        for fila in datos:
            escritor_csv.writerow(fila)
    
    print("Los datos se han guardado en 'datos.csv'")
else:
    print("No se pudo acceder a la página web")
