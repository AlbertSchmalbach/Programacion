import socket

def get_gateway_address():
    try:
        # Obtener el nombre del host
        host_name = socket.gethostname()

        # Obtener la dirección IP de la máquina
        host_ip = socket.gethostbyname(host_name)

        # Obtener la información de la interfaz de red predeterminada
        gateway_ip = socket.gethostbyname(socket.getfqdn(socket.gethostname()))

        return gateway_ip
    except Exception as e:
        return str(e)

# Obtener la dirección de la puerta de enlace
gateway_address = get_gateway_address()

if gateway_address:
    print("La dirección de la puerta de enlace es:", gateway_address)
else:
    print("No se pudo obtener la dirección de la puerta de enlace.")
