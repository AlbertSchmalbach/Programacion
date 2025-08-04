def calcular_horario_llegada(hora_salida,minutos_salida,segundos_salida,hora_duracion,minutos_duracion,segundos_duracion):

    hora_llegada = hora_salida + hora_duracion
    minutos_llegada = minutos_salida + minutos_duracion
    segundos_llegada = segundos_salida + segundos_duracion

    if segundos_llegada >= 60:
        segundos_llegada = segundos_llegada - 60
        minutos_llegada+=1


    if minutos_llegada >= 60:
        minutos_llegada = minutos_llegada - 60
        hora_llegada +=1


    if hora_llegada >= 24:
        hora_llegada = hora_llegada - 24


    tiempo_llegada = f"{hora_llegada}:{minutos_llegada}:{segundos_llegada}"

    print (tiempo_llegada)
    return tiempo_llegada



calcular_horario_llegada(7,3,58,0,24,33)