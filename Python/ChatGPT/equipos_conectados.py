from scapy.all import ARP, Ether, srp

# Para que este codigo funcione es necesario instalar WinPcap podemos descargarlo e instalarlo https://www.winpcap.org/install/

def scan(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    return devices

ip_range = "192.168.1.1/24"  # Cambia esto a tu rango de IP local

devices = scan(ip_range)
for device in devices:
    print(f"IP: {device['ip']} - MAC: {device['mac']}")
