import platform
import socket
import requests
import cpuinfo
import psutil
import uuid


def get_system_info():

    def get_size(bytes, suffix="B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f} {unit}{suffix}"
            bytes /= factor

    system_info = {}
    system_info['Sistema Operativo'] = platform.system()
    system_info['Versión del SO'] = platform.release()

    
    system_info['Board'] = platform.uname().machine
    system_info['CPU'] = cpuinfo.get_cpu_info()['brand_raw']
    system_info['Núcleos de CPU'] = psutil.cpu_count(logical=False)
    system_info['RAM Total (GB)'] = round(
        psutil.virtual_memory().total / (1024**3), 2)
    
    partitions = psutil.disk_partitions()
    for partition in partitions:
        partition_usage = psutil.disk_usage(partition.mountpoint)
        system_info['Tamaño Disco'] = get_size(partition_usage.total)
    
    host_name = socket.gethostname()
    system_info['Nombre del Host'] = host_name
    system_info['Dirección IP'] = socket.gethostbyname(host_name)
    system_info['Direccion MAC'] = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])

    # Obtenemos direccion ip publica por medio de una api
    response = requests.get('https://api64.ipify.org?format=json')
    data = response.json()
    system_info['Dirección IP Pública'] = data['ip']

    return system_info


info = get_system_info()
for key, value in info.items():
    print(f"{key}: {value}")
