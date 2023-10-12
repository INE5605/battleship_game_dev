from embarcacao.embarcacao import Embarcacao

class Bote(Embarcacao):
    def __init__(self, tamanho = 1):
        super().__init__(tamanho)