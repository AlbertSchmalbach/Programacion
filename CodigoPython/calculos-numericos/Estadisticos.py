class Estadisticas:
    def __init__(self, datos):
        self.datos = datos

    def calcular_promedio(self):
        if not self.datos:
            return 0
        return round((sum(self.datos) / len(self.datos)),2)

    def calcular_mediana(self):
        if not self.datos:
            return 0
        datos_ordenados = sorted(self.datos)
        n = len(datos_ordenados)
        mitad = n // 2
        
        if n % 2 == 0:
            mediana = (datos_ordenados[mitad - 1] + datos_ordenados[mitad]) / 2
        else:
            mediana = datos_ordenados[mitad]
        
        return mediana

# Ejemplo de uso:
datos = [81, 89, 92, 85, 93, 62, 85, 105, 90]
estadisticas = Estadisticas(datos)

print("Promedio:", estadisticas.calcular_promedio())  
print("Mediana:", estadisticas.calcular_mediana())    
