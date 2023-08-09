class Punto:
    def __init__(self,x:int,y:int):
            self.x: int = x
            self.y: int= y


if __name__ =="__main__":
    mi_punto = Punto(3, 6)

    print("cordenadas:", mi_punto.x, ",",mi_punto.y)