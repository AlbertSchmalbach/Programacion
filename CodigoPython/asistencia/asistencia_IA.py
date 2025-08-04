import os
import pandas as pd
from pathlib import Path

try:
    # Obtén la ruta de la carpeta de recursos
    resource_folder = Path(__file__).parent / 'resources'

    # Nombres de los archivos
    name_csv1 = resource_folder / '6013284755 - Poll Report.csv'
    name_csv2 = resource_folder / 'report_poll.csv'
    asistencia_csv = Path('asistencia.csv')

    # Renombrar el archivo según su existencia
    if name_csv1.exists():
        name_csv1.rename(asistencia_csv)
    elif name_csv2.exists():
        name_csv2.rename(asistencia_csv)
    else:
        raise FileNotFoundError("No se encontró ningún archivo de reporte.")

    # Leer y procesar el archivo CSV
    with asistencia_csv.open(encoding='utf-8') as file_csv:
        list_csv = file_csv.readlines()

    new_file_csv = []
    for index, line in enumerate(list_csv):
        if line.strip() in ['Asistencia de Reunión', 'Detalles de la encuesta']:
            new_file_csv = list_csv[index+1:]
            break

    if not new_file_csv:
        raise ValueError("No se encontraron encabezados esperados en el archivo CSV.")

    # Escribir el archivo procesado
    with open('file_csv_new.csv', 'w', encoding='utf-8') as new_csv:
        new_csv.writelines(new_file_csv)

    # Leer el archivo procesado con pandas
    df_asistencia = pd.read_csv('file_csv_new.csv')
    df_asistencia = df_asistencia.rename(columns={'Nombre de usuario':'Familia', 'Cantidad de asistentes(solo numero)':'Cantidad'})
    datos_asistencia = df_asistencia[['Familia', 'Cantidad']]

    print()
    print('**************** DATOS ASISTENTES *****************')
    print(datos_asistencia)
    print()

    try:
        total_asistencia = pd.to_numeric(df_asistencia["Cantidad"], errors='coerce').sum()
        print(f'ASISTENCIA TOTAL POR ZOOM: {total_asistencia}')
    except Exception as e:
        print(f'Error al sumar la asistencia: {e}')

    print()

except FileNotFoundError as fnf_error:
    print(f"Error de archivo no encontrado: {fnf_error}")
except ValueError as val_error:
    print(f"Error de valor: {val_error}")
except Exception as e:
    print(f'Ocurrió un error: {e}')
