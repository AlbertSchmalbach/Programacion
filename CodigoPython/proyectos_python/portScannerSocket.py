import sys
import socket
from datetime import datetime

def main():
    target = "192.168.1.43"
    port_min = int(input('Ingrese el numero de puerto de inicio: '))
    port_max = int(input('Ingrese el numero de puerto final: '))
    print("*"*46)
    print(f"la IP es: {target}")
    print(f"Inicio de escaneo: {datetime.now}")
    print("*"*46)

    for port in range(port_min, port_max):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))

        if result == 0:
            print(f'(+)El puerto {port} se encuentra abierto')
        s.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()