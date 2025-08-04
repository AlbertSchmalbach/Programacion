import pandas as pd
from faker import Faker

def crear_datos(cantidad):
    datos_ficticio = Faker()
    datos= {}

    for i in range(cantidad):
        name = datos_ficticio.name()
        adress = datos_ficticio.address()
        datos[name] = adress
    
    return datos

def generar_df(diccionario):
    df = pd.DataFrame([[key, diccionario[key]] for key in diccionario.keys()], columns = ['name', 'address'])
    return df

def crear_csv(df, ficheros='datos'):
    nombre_fichero = ficheros+'.csv'
    df.to_csv(nombre_fichero,encoding='utf-8')


if __name__ == '__main__':
    datos = crear_datos(5)
    df = generar_df(datos)
    print(df.head())
    crear_csv(df, 'pruebas')