from datetime import datetime

fecha = datetime(2023,2,18)
fecha_hoy = datetime.now()
fecha_str = datetime.strptime("2023-02-18", "%Y-%m-%d")
print(fecha.strftime("%Y-%m-%d"))