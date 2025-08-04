from datetime import datetime, timedelta

fecha1 = datetime(2023, 1, 1) + timedelta(weeks=2)
fecha2 = datetime(2023, 2, 1)

delta = fecha2 - fecha1

print(fecha1)
print(delta)
print("dias", delta.days)
