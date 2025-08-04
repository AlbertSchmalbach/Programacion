import socket

def check_host(hostname):
    try:
        host_ip = socket.gethostbyname(hostname)
        socket.create_connection((host_ip, 80), timeout=2)
        return True
    except (socket.gaierror, socket.error):
        return False

host_to_check = "192.168.1.1" # Cambia esto al host que quieras verificar

if check_host(host_to_check):
    print(f"El host {host_to_check} está en línea.")
else:
    print(f"El host {host_to_check} no está en línea.")
