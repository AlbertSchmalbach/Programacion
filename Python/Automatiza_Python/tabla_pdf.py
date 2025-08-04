"""
Script para extraer la primera tabla de un PDF y exportarla a varios formatos.
Requiere: camelot-py, pandas, openpyxl, opencv-python-headless

Asegúrate de tener instalado camelot-py y sus dependencias:
    pip install camelot-py[cv]

Si tienes problemas de importación en VS Code, verifica que el intérprete de Python sea el correcto.
"""

import sys

try:
    import camelot
except ImportError:
    print("Error: No se pudo importar camelot. Verifica la instalación y el intérprete de Python.")
    sys.exit(1)

PDF_PATH = 'tb_productos.pdf'

try:
    # Leer el PDF y extraer tablas
    tables = camelot.read_pdf(PDF_PATH, pages='1')
    print(f"Número de tablas encontradas: {len(tables)}")
    if len(tables) == 0:
        print("No se encontraron tablas en el PDF.")
        sys.exit(1)
    # Mostrar la primera tabla extraída
    print(tables[0].df)
    # Exportar la primera tabla a varios formatos
    tables[0].to_csv('product.csv')
    tables[0].to_json('product.json')
    tables[0].to_excel('product.xlsx')
    tables[0].to_html('product.html')
    tables[0].to_markdown('product.md')
    print("Exportación completada correctamente.")
except Exception as e:
    print(f"Ocurrió un error al procesar el PDF: {e}")
    sys.exit(1)

