class Bola:
    def __init__(self, cor, circunferencia, material):
        self._cor = cor
        self._circunferencia = circunferencia
        self._material = material

    def trocarCor(self, novaCor):
        self._cor = novaCor

    def mostrarCor(self):
        print(self._cor)

bola = Bola("Branca", 45, "Elastico")

bola.mostrarCor()
bola.trocarCor("Azul")
bola.mostrarCor()

