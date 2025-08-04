import pickle

# Creacion de fichero binario
# lista_nombres = ["Luz Saray", "Yulisa", "Pablo", "Misuris Paola", "Sofia"]

# fichero_bin = open("lista_nombres", "wb")

# pickle.dump(lista_nombres, fichero_bin)

# fichero_bin.close()

# Leer fichero binario
fichero = open("lista_nombres", "rb")

lista = pickle.load(fichero)

print(lista)