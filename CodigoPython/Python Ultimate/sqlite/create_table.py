import sqlite3

path = r"C:\Users\KHAdmin\Documents\CarpetaProtegida\Albert\Archivos\Script_Python\Python Ultimate\sqlite\app.db"
conexion = sqlite3.connect(path)
cursor = conexion.cursor()
cursor.execute(
    """
        CREATE TABLE if not exists productos (id INTEGER primary key, nombre VARCHAR(20), valor FLOAT);
    """
)
conexion.commit()
conexion.close()