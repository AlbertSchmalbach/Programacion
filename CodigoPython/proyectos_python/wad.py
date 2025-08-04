import subprocess
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help='Indicar la URL \n(ej https://ejemplo.com)')
parser = parser.parse_args()

def main():
    if parser.target:
        subprocess.run("wad -u" + parser.target+"> tecnologias.txt", shell=True)
        tecnos = open('tecnologias.txt', 'r')
        tecnos = tecnos.read()
        tecnos = tecnos.split('[')
        tecnos = tecnos[1].split(']')
        tecnos = tecnos[0].split('{')
        
        for tecnologia in tecnos:
            nuevo = tecnologia.replace('\n', '')
            nuevo = nuevo.replace('           ', '')
            nuevo = nuevo.replace('"', '')
            nuevo = nuevo.split('}')
            nuevo = nuevo[0]
            nuevo = nuevo.replace(',', '\n')
            print(nuevo)
            print('*'*60)

    else:
        print('(-) Ingresa una URL')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()