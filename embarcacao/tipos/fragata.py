from embarcacao.embarcacao import Embarcacao

class Fragata(Embarcacao):
    def __init__(self, tamanho = 3, letra = "F"):
        super().__init__(tamanho, letra)