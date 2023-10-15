from embarcacao.embarcacao import Embarcacao

class Bote(Embarcacao):
    def __init__(self, tamanho = 1, letra = "B"):
        super().__init__(tamanho, letra)