import os

shutdown = input("¿Quieres apagar el portatil? (si/no): ")

if shutdown.lower() == "si":
    os.system("shutdown /s /t 10")
else:
    exit()