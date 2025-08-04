# 1. Script para cifrar el archivo

def cifrado_cesar(texto, clave):
    resultado = ""
    for char in texto:
        if char.isalpha():
            inicio = ord('a') if char.islower() else ord('A')
            resultado += chr((ord(char) - inicio + clave) % 26 + inicio)
        else:
            resultado += char
    return resultado

def encriptar_archivo(archivo_entrada, archivo_salida, clave):
    with open(archivo_entrada, 'r') as f:
        contenido = f.read()

    contenido_encriptado = cifrado_cesar(contenido, clave)

    with open(archivo_salida, 'w') as f:
        f.write(contenido_encriptado)

# 2. Script para desifrar un archivo
        
def descifrado_cesar(texto, clave):
    return cifrado_cesar(texto, -clave)

def desencriptar_archivo(archivo_entrada, archivo_salida, clave):
    with open(archivo_entrada, 'r') as f:
        contenido_encriptado = f.read()

    contenido_desencriptado = descifrado_cesar(contenido_encriptado, clave)

    with open(archivo_salida, 'w') as f:
        f.write(contenido_desencriptado)

# Encriptar el archivo
archivo_entrada = 'usuario.txt'
archivo_salida = 'usuario_encriptado.txt'
clave = 3  # Puedes cambiar la clave según tu preferencia

# Desencriptar el archivo
archivo_encriptado = 'usuario_encriptado.txt'
archivo_desencriptado = 'usuario_desencriptado.txt'
clave = 3  # Debe coincidir con la clave usada para encriptar

# encriptar_archivo(archivo_entrada, archivo_salida, clave)
desencriptar_archivo(archivo_encriptado, archivo_desencriptado, clave)
