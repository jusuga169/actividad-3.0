import math


class Circulo:
    def __init__(self, centro: int, radio: int):
        self.centro: int = centro
        self.radio: int = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def punto_pertenece(self, punto: int):
        distancia = math.sqrt((punto[0] - self.centro[0]) ** 2 + (punto[1] - self.centro[1]) ** 2)
        return distancia <= self.radio

if __name__ == "__main__":
    centro = (0, 0)
    radio = 5
    circulo = Circulo(centro, radio)

    print("Área del círculo:", circulo.calcular_area())
    print("Perímetro del círculo:", circulo.calcular_perimetro())

    punto1 = (3, 4)
    punto2 = (0, 6)

    print("¿El punto", punto1, "pertenece al círculo?", circulo.punto_pertenece(punto1))
    print("¿El punto", punto2, "pertenece al círculo?", circulo.punto_pertenece(punto2))


