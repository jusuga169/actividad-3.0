class Carta:

    CORAZON = "Corazón"
    DIAMANTE = "Diamante"
    TREBOL = "Trébol"
    ESPADA = "Espada"

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

if __name__ == "__main__":
    carta1 = Carta(10, Carta.CORAZON)
    carta2 = Carta(4, Carta.TREBOL)

    print("Carta 1 - Valor:", carta1.valor, "- Pinta:", carta1.pinta)
    print("Carta 2 - Valor:", carta2.valor, "- Pinta:", carta2.pinta)