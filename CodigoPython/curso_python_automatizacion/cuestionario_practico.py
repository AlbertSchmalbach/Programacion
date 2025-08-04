# 1. La función create_python_script crea un nuevo script de Python en el directorio de trabajo actual, le añade la línea de comentarios declarada por la variable 'comments' y devuelve el tamaño del nuevo archivo. Rellena los huecos para crear un script llamado "programa.py".

def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "w") as file:
        file.write(comments)
        filesize = len(comments)
    return(filesize)

print(create_python_script("program.py"))

# 2. La función nuevo_directorio crea un nuevo directorio dentro del directorio de trabajo actual, luego crea un nuevo archivo vacío dentro del nuevo directorio, y devuelve la lista de archivos en ese directorio. Rellena los huecos para crear un archivo "script.py" en el directorio "PythonPrograms". 

import os

def new_directory(directory, filename):
    # Before creating a new directory, check to see if it already exists
    if os.path.isdir(directory) == False:
        os.mkdir(directory)

    # Create the new file inside of the new directory
    os.chdir(directory)
    with open (filename, "w") as file:
        pass
    # Return the list of files in the new directory
    return os.listdir(os.getcwd())

print(new_directory("PythonPrograms", "script.py"))

# 3. La función fecha_archivo crea un nuevo archivo en el directorio de trabajo actual, comprueba la fecha en que se modificó el archivo y devuelve sólo la parte de fecha de la marca de tiempo en el formato aaaa-mm-dd. Rellene los campos para crear un archivo llamado "archivo_nuevo.txt" y compruebe la fecha en que se modificó.

import datetime

def file_date(filename):
  # Create the file in the current directory
    with open(filename, "w") as file:
        file.write('')
    timestam = os.path.getmtime(filename)
    # Convert the timestamp into a readable format, then into a string
    date = datetime.datetime.fromtimestamp(timestam)
    # Return just the date portion 
    # Hint: how many characters are in “yyyy-mm-dd”? 
    return ("{:%Y-%m-%d}".format(date))

print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd

# 4. La función directorio_padre devuelve el nombre del directorio que se encuentra justo encima del directorio de trabajo actual. Recuerde que '..' es un alias de ruta de acceso relativa que significa "subir al directorio principal". Rellena los huecos para completar esta función.

def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  relative_parent = os.path.join('..', os.getcwd())

  # Return the absolute path of the parent directory
  return relative_parent

print(parent_directory())