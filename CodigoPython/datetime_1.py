from datetime import date
import time

today = date.today()

print("Hoy:", today)
print("Año:", today.year)
print("Mes:", today.month)
print("Día:", today.day)
    

my_date = date(2019, 11, 4)
print(my_date)

timestamp = time.time()
print("Marca de tiempo:", timestamp)

d = date.fromtimestamp(timestamp)
print("Fecha:", d)

fecha = date.fromisoformat('1990-11-18')

print(fecha)

d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)

d = date(2019, 11, 4)
print(d.weekday())
    