import sqlite3

path = r"C:\Users\KHAdmin\Documents\CarpetaProtegida\Albert\Archivos\Script_Python\Python Ultimate\sqlite\app.db"

with sqlite3.connect(path) as conexion:
    cursor = conexion.cursor()
    usuarios = [
        (2, "Alberto Schmalbach"),
        (3, "Jesus Atencia"),
        (4, "Luz Karime Oviedo"),
        (5, "Misuri Atencia")
    ]
    cursor.executemany(
        "INSERT INTO usuarios values(?, ?)",
        usuarios,
    )
