class  Vehiculo:
    def __init__(self, velocidad_maxima:int , kilometraje:int):
        self.velocidad_maxima: int = velocidad_maxima
        self.kilometraje:int  = kilometraje


if __name__ == "__main__":
    mi_auto = Vehiculo(200, 50000)

    print("velocidad maxima:", mi_auto.velocidad_maxima, "km/h")
    print("kilometraje", mi_auto.kilometraje, "km")