import os
import pandas as pd
from pathlib import Path

try:

    name_csv1 = '6013284755 - Poll Report.csv' 
    name_csv2 = 'report_poll.csv'

    if os.path.exists(name_csv1):
        os.rename(name_csv1, 'asistencia.csv')
    else:
         os.rename(name_csv2, 'asistencia.csv')
        
    with open('asistencia.csv', encoding='utf-8') as file_csv:
        list_csv = file_csv.readlines()
    

        for index, line in enumerate(list_csv):
                if line == 'Asistencia de Reunión\n' or line == 'Detalles de la encuesta\n':
                    new_file_csv = list_csv[index+1:]
    
        with open('file_csv_new.csv', 'w', encoding='utf-8') as new_csv:
            new_csv.writelines(new_file_csv)
        

    df_asistencia = pd.read_csv('file_csv_new.csv', delimiter=',')
    df_asistencia = df_asistencia.rename(columns={'Nombre de usuario':'Familia', 'Cantidad de asistentes(solo numero)':'Cantidad'})
    datos_asistencia = df_asistencia[['Familia', 'Cantidad']]

    print()
    print('**************** DATOS ASISTENTES *****************')
    print()
    print(datos_asistencia)
    print()

    try:
        print(f'ASISTENCIA TOTAL POR ZOOM: {df_asistencia["Cantidad"].sum()}')
    except:
         print('Hay algun dato no numerico en la columna')

    print()

except:
    print('Archivo no encontrado')


