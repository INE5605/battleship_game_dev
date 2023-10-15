from embarcacao.embarcacao import Embarcacao

class PortaAvioes(Embarcacao):
    def __init__(self, tamanho = 4, letra = 'P'):
        super().__init__(tamanho, letra)