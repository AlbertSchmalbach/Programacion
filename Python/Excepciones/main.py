try:
    # Código que podría generar una excepción
    pass
except: #TipoExcepcion:
    # Acciones a realizar en caso de excepción
    pass

# Manejo de Múltiples Excepciones

try:
    numero = int("abc")
except ValueError:
    print("Se produjo un ValueError")
except TypeError:
    print("Se produjo un TypeError")

# Bloque Finally y Cierre de Archivos

try:
    archivo = open("archivo.txt", "w")
    # Hacer algo con el archivo
except IOError:
    print("Error al abrir el archivo")
finally:
    archivo.close()  # Siempre se cerrará el archivo

# Utilizar ELSE con Try y Except

try:
    # Código que puede generar una excepción
    print("Hello")
except:
    # Manejo de la excepción
    print("Something went wrong")
else:
    # Ejecutado si no ocurre ninguna excepción
    print("Nothing went wrong")

# Levantar una Excepción

def dividir(x, y):
    if y == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return x / y

print(dividir(5,0))