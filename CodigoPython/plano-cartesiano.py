class Punto:

    # Constructor de clase
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        elif self.x == 0 and self.y != 0:
            return "Sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre el eje X"
        else:
            return "En el origen"
        
    def vector(self, otro_punto):
        return Punto(otro_punto.x - self.x, otro_punto.y - self.y)
        

class Rectangulo:
    def __init__(self, b=0, a=0):
        self.bas = b
        self.alt = a

    def base(self):
        return self.bas
    
    def altura(self):
        return self.alt
    
    def area(self):
        ar = self.bas * self.alt
        return ar
    
# Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
A = Punto(2, 3)
B = Punto(5,5)
C = Punto(-3, -1)
D = Punto(0,0)
print('A',A)
print('B',B)
print('C',C)
print('D',D)

# Consulta a que cuadrante pertenecen el punto A, C y D.
print(A.cuadrante())
print(B.cuadrante())
print(D.cuadrante())

# Consulta los vectores AB y BA.
print(A.vector(B))
print(B.vector(A))

# Crea un rectángulo utilizando los puntos A y B.
vector = A.vector(B)
rect1 = Rectangulo(vector.x, vector.y)
print(rect1.base())
print(rect1.altura())
print(rect1.area())


