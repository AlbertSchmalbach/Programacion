from datetime import datetime, timedelta
import locale, pytz

dt = datetime.now() # Fecha y hora actual


# print(dt) 
# print(dt.year)  # año
# print(dt.month) # mes
# print(dt.day)  # día

# print(dt.hour) # hora
# print(dt.minute) # minutos
# print(dt.second) # segundos
# print(dt.microsecond) # microsegundos

# print("{}:{}:{}".format(dt.hour, dt.minute, dt.second))
# print("{}/{}/{}".format(dt.day, dt.month, dt.year))

# dt = datetime(2024, 1,1,0,0)
# dt.replace(year=2025)
# print(dt)
# print(dt.isoformat())

# print(dt.strftime("%A %d %B %Y %I:%M"))

# Idioma "es-ES" (código para el español de España)
# locale.setlocale(locale.LC_ALL, 'es-co') 

# print(dt.strftime("%A %d %B %Y %I:%M"))
# print(dt.strftime("%A %d de %B del %Y - %H:%M"))  # %I 12h - %H 24h

# print(locale.locale_alias)

# OPERACIONES

print(dt.strftime("%A %d de %B del %Y - %H:%M")) # nombredia numerodia de Mes del Año - Horas:Minutos

# Generamos 14 días con 4 horas y 1000 segundos de tiempo
t = timedelta(days=14, hours=4, seconds=1000)

# Lo operamos con el datetime de la fecha y hora actual
dentro_de_dos_semanas = dt + t
print(dentro_de_dos_semanas.strftime("%A %d de %B del %Y - %H:%M"))
hace_dos_semanas = dt - t
print(hace_dos_semanas.strftime("%A %d de %B del %Y - %H:%M"))


# print(pytz.all_timezones)

dt = datetime.now(pytz.timezone('America/Bogota'))
print(dt.strftime("%A %d de %B del %Y - %H:%M"))