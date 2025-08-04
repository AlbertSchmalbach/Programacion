# from datetime import date, datetime, timezone, timedelta

# fecha_actual = date.today()

# # print(fecha_actual)

# fecha_en_texto = '{}/{}/{}'.format(fecha_actual.day, fecha_actual.month, fecha_actual.year)
# fecha_en_texto = fecha_actual.strftime('%d/%m/%Y')
# # print(fecha_en_texto)

# fecha_hora_actual = datetime.now()
# # print(fecha_hora_actual)

# fecha_hora_actual_texto = fecha_hora_actual.strftime('%d/%m/%Y %H:%M')
# # print(fecha_hora_actual_texto)

# fecha_hora_texto = '01/09/2024 12:30'
# fecha_hora = datetime.strptime(fecha_hora_texto, '%d/%m/%Y %H:%M')
# # print(fecha_hora)

# Fecha Global
# fecha_hora_actual = datetime.now()

# # Paso 1 timedelta
# diferencia = timedelta(hours=-5)
# # print(diferencia)

# # Paso 2 timezone
# zona_horaria = timezone(diferencia)
# # print(zona_horaria)

# # Paso 3 astimezone
# fecha_hora_bogota = fecha_hora_actual.astimezone(zona_horaria)
# fecha_hora_bogota_texto = fecha_hora_bogota.strftime('%d/%m/%Y %H:%M')
# print(fecha_hora_bogota_texto)

from datetime import datetime
from pytz import timezone

fecha_y_hora_actuales = datetime.now()
zona_horaria = timezone('America/Bogota')
fecha_y_hora_bogota = fecha_y_hora_actuales.astimezone(zona_horaria)
fecha_y_hora_bogota_en_texto = fecha_y_hora_bogota.strftime('%d/%m/%Y %H:%M')

print(fecha_y_hora_bogota_en_texto)