import math

class Punto:

    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def mostrar(self, x: int, y: int):
        print("coordenadas:", pe.x, ",", pe.y)

    def mover(self, nuevo_x: int, nuevo_y: int):
        self.x: int = nuevo_x
        self.y: int = nuevo_y
        print("el punto ha sido movido a las coordenadas", self.x, ",", self.y)

    def calcular_distancia(self, otro_punto: int):
        distancia = math.sqrt((self.x-otro_punto.x)**2 + (self.y-otro_punto.y)**2)
        return distancia


if __name__ == "__main__":

    pe: Punto = Punto(1,10)
    pe2: Punto = Punto(7,10)

    print("coordenadas:", pe.x, "," ,pe.y)

    pe.mover(10,12)

    distancia = pe.calcular_distancia(pe2)
    print("distancia entre los puntos:", distancia)