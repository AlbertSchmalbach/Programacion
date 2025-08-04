import datetime

# Salida de Fecha

# %Y : Año con siglo como un número decimal de cuatro dígitos.
# %m : Mes como número decimal (01, 02, …, 12).
# %d : Día del mes como número decimal (01, 02, …, 31).
# %H : Hora (00, 01, …, 23).
# %M : Minuto (00, 01, …, 59).
# %S : Segundo (00, 01, …, 59).

# Creación de Objetos de Fecha

fecha_actual = datetime.date(2025,7,28)
print(fecha_actual)

# El Método strftime()

cadena_fecha = fecha_actual.strftime("%Y/%m/%d")
print(cadena_fecha)

