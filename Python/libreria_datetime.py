from datetime import date, time, datetime, timedelta

fecha = date(2023, 6, 20)
hora = time(14, 40, 20)
fecha_hora = datetime(2023, 6, 20, 14, 40, 20)
# print(fecha_hora)

# 1. date.today()
print(date.today())
# 2. datetime.now()
dt = datetime.now()
print(dt)
# 3. dt.year()
print(dt.year)
# 4. dt.month
print(dt.month)
# 5. dt.day
print(dt.day)
# 6. dt.weekday
print(dt.weekday())
# 7. dt.hour
print(dt.hour)
# 8. dt.second
print(dt.second)
# 9. dt.microsecond
print(dt.microsecond)

# Conversión de fechas en cadenas con diferentes formatos

# %Y (año completo)
# %y (últimos dos dígitos del año) 
# %m (mes en número)
# %B (mes en palabra)
# %d (día)
# %A (día de la semana)
# %a (día de la semana abrevidado)
# %H (hora en formato 24 horas)
# %I (hora en formato 12 horas)
# %M (minutos)
# %S (segundos) 
# %p (AM o PM)
# %C (fecha y hora completas)
# %x (fecha completa)
# %X (hora completa)

# d.strftime(formato)

print(dt.strftime('%d-%m-%Y'))
print(dt.strftime('%A, %d %B, %y'))
print(dt.strftime('%H:%M:%S'))
print(dt.strftime('%H horas, %M minutos y %S segundos'))

# Conversión de cadenas en fechas

# strptime(s, formato) 

print(datetime.strptime('17/6/2023', '%d/%m/%Y'))
print(datetime.strptime('2023-6-17 14:50:30', '%Y-%m-%d %H:%M:%S'))

# Aritmética de fechas

# 1. timedelta(dias, segundos, microsegundos)
d1 = datetime(2023, 6, 1)
d2 = timedelta(31, 3600)
print(d1 + d2)
print(datetime.now() - d1)
print(timedelta(days=132, seconds=1826, microseconds=895590))