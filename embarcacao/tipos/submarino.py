from embarcacao.embarcacao import Embarcacao

class Submarino(Embarcacao):
    def __init__(self, tamanho = 2, letra = 'S'):
        super().__init__(tamanho, letra)