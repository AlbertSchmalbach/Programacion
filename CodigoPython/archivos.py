def createFiles():

    archivo = open('archivo.txt', 'w', encoding='utf-8')

    for i in range(10):
        archivo.write(f'Linea de escritura # {i + 1} \r\n')

    archivo.close()


def openFiles():

    with open('archivo.txt', encoding='utf-8') as file:
        print(file.read())

createFiles()
openFiles()