archivo_texto = open("Archivos/texto.txt", "r+")

linea_texto = archivo_texto.readlines()

linea_texto[1] = "Es compartir lo que pensamos, lo que sentimos, lo que nos preocupa."

archivo_texto.seek(0)

archivo_texto.writelines(linea_texto)

archivo_texto.close()