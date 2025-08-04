import socket
from cleaner import cleaning

cleaning()

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print(IPAddr) #192.168.1.38