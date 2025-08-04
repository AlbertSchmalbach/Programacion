# Crear archivo saludo.txt
archivo = open("Archivos\saludo.txt", "w", encoding="utf-8") #Crea nuevo archivo
texto = "Alberto Schmalbach\nMagangue, Bol."
archivo.write(texto) #añade texto al archivo
archivo.close() #Cierra archivo

with open("Archivos\saludo.txt", "w", encoding="utf-8") as archivo:
    texto = "Alberto Schmalbach\nMagangue, Bol."
    archivo.write(texto)

# Leer saludo.txt
with open("Archivos\saludo.txt", "r") as archivo:
    num_line = 0
    for line in archivo:
        num_line+=1
        if line[num_line] == "g":
            print(line)
    
    print(num_line)
    