def mejor_del_salon(std1:dict, std2:dict, std3:dict, std4:dict, std5:dict) -> str:
    
    def prom_nota(std:dict):
        t = []
        for n in std.values():
            if isinstance(n, float):
                t.append(n)
        prom = round(sum(t)/len(t),2)
        return prom  

    def nombre_menor_alfabeticamente(nombres):
        for name in nombres:
            if not isinstance(name, float):
                return min(name)  
            
    # Lista que contendra el nombre de los mejores alumnos con mejor promedio
    alumnos = []
    # Lista de promedios de los alumnos
    media_notas = [prom_nota(std1), prom_nota(std2), prom_nota(std3), prom_nota(std4), prom_nota(std5)]
    # promedio mayor
    max_nota = max(media_notas)
    
    if max_nota == prom_nota(std1):
        alumnos.append(std1['nombre'])
    if max_nota == prom_nota(std2):
        alumnos.append(std2['nombre']) 
    if max_nota == prom_nota(std3):
        alumnos.append(std3['nombre'])
    if max_nota == prom_nota(std4):
        alumnos.append(std4['nombre'])
    if max_nota == prom_nota(std5):
        alumnos.append(std5['nombre'])


    alumnos = [alumnos, media_notas]

    mejor_alumno = nombre_menor_alfabeticamente(alumnos)

    return mejor_alumno    

# est_1 = {"nombre":"Luz Saray",
#          "matematicas":4.5,
#          "espanol":4.2,
#          "ciencias": 3.6,
#          "literatura":4.2,
#          "arte": 3.8}
# est_2 = {"nombre":"Catalina",
#          "matematicas":4.2,
#          "espanol":4.2,
#          "ciencias": 3.6,
#          "literatura":4.2,
#          "arte": 3.8}
# est_3 = {"nombre":"Maria",
#          "matematicas":3.5,
#          "espanol":3.2,
#          "ciencias": 4.6,
#          "literatura":3.2,
#          "arte": 3.2}
# est_4 = {"nombre":"Jose",
#          "matematicas":3.5,
#          "espanol":3.7,
#          "ciencias": 4.6,
#          "literatura":4.0,
#          "arte": 3.1}
# est_5 = {"nombre":"Paola",
#          "matematicas":3.8,
#          "espanol":3.2,
#          "ciencias": 3.2,
#          "literatura":3.9,
#          "arte": 4.0}

std1 = {'nombre': 'pablo', 'matematicas': 3.4, 'español': 5.0, 'ciencias': 2.9, 'literatura': 4.2, 'arte': 3.2}
std2 = {'nombre': 'andres', 'matematicas': 2.1, 'español': 5.0, 'ciencias': 3.0, 'literatura': 4.1, 'arte': 3.5}
std3 = {'nombre': 'daniela', 'matematicas': 5.0, 'español': 4.2, 'ciencias': 4.4, 'literatura': 3.5, 'arte': 4.7}
std4 = {'nombre': 'maria', 'matematicas': 3.2, 'español': 3.7, 'ciencias': 3.1, 'literatura': 4.7, 'arte': 3.4}
std5 = {'nombre': 'Pedro', 'matematicas': 5.0, 'español': 4.2, 'ciencias': 4.4, 'literatura': 3.5, 'arte': 4.7}



alumno = mejor_del_salon(std1, std2, std3, std4, std5)
print(f'El mejor alumno es: {alumno}')