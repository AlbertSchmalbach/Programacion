import sqlite3

path = r"C:\Users\KHAdmin\Documents\CarpetaProtegida\Albert\Archivos\Script_Python\Python Ultimate\sqlite\app.db"

with sqlite3.connect(path) as conexion:
    cursor = conexion.cursor()
    cursor.execute(
        """
            CREATE TABLE if not exists usuarios (id INTEGER primary key, nombre VARCHAR(20));
        """
    )
