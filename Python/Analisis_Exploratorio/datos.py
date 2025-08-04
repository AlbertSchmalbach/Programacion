import pandas as pd
import os

# Datos para la primera hoja
data_hoja1 = {
    "Nombre": [
        "Carlos López", "María Pérez", "Juan Martínez", "Ana Gómez", "Pedro Díaz",
        "Laura Sánchez", "José Romero", "Andrea Ruiz", "Luis Torres", "Carmen Silva",
        "Miguel Ríos", "Sofía Mendoza", "Ricardo Herrera", "Elena Moreno", "David Ortiz"
    ],
    "Fecha de nacimiento": [
        "15/05/1985", "23/08/1990", "12/11/1978", "03/03/1983", "19/07/1987",
        "28/06/1992", "10/09/1980", "25/12/1984", "09/01/1975", "18/04/1988",
        "30/10/1982", "05/02/1993", "27/07/1981", "14/12/1995", "22/03/1979"
    ],
    "Sueldo (COP)": [
        2500000, 3100000, 2900000, 2800000, 2700000,
        3500000, 2650000, 3000000, 3200000, 2750000,
        2950000, 3450000, 3300000, 3150000, 2850000
    ]
}

# Datos para la segunda hoja
data_hoja2 = {
    "Fecha": [
        "01/11/2024", "02/11/2024", "03/11/2024", "04/11/2024", "05/11/2024",
        "06/11/2024", "07/11/2024", "08/11/2024", "09/11/2024", "10/11/2024",
        "11/11/2024", "12/11/2024", "13/11/2024", "14/11/2024", "15/11/2024"
    ],
    "Categoría": [
        "Electrodomésticos", "Muebles", "Ropa", "Tecnología", "Juguetes",
        "Ropa", "Electrodomésticos", "Muebles", "Tecnología", "Ropa",
        "Juguetes", "Muebles", "Electrodomésticos", "Tecnología", "Ropa"
    ],
    "Procedencia": [
        "Nacional", "Importado", "Nacional", "Importado", "Nacional",
        "Nacional", "Importado", "Nacional", "Importado", "Nacional",
        "Nacional", "Importado", "Nacional", "Importado", "Nacional"
    ],
    "Vendedor": [
        "Juan Pérez", "Ana Díaz", "Carlos Gómez", "Laura Sánchez", "Pedro Martínez",
        "Andrea Ruiz", "José Torres", "Carmen Silva", "Miguel Ríos", "Luis Mendoza",
        "Elena Moreno", "David Ortiz", "Ricardo Herrera", "Sofía Romero", "María López"
    ],
    "Ingreso Neto (COP)": [
        1250000, 1800000, 950000, 2200000, 1500000,
        1200000, 2000000, 1300000, 2400000, 1050000,
        1400000, 1850000, 1750000, 2300000, 1000000
    ],
    "IVA (COP)": [
        237500, 342000, 180500, 418000, 285000,
        228000, 380000, 247000, 456000, 199500,
        266000, 351500, 332500, 437000, 190000
    ]
}

# Crear las hojas en un archivo Excel

ruta_archivo = os.getcwd() + 'productos.xlsx'
with open(ruta_archivo, "w") as file:
    pd.DataFrame(data_hoja1).to_excel(file, index=False, sheet_name='Datos Personales')
    pd.DataFrame(data_hoja2).to_excel(file, index=False, sheet_name='Transacciones')
# ruta_archivo
