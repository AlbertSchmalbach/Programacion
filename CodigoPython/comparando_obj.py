class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, otro) -> bool:
        return self.lat == otro.lat and self.lon == otro.lon
    

cord1 = Coordenadas(45,70)
cord2 = Coordenadas(45,70)
print(cord1 == cord2)