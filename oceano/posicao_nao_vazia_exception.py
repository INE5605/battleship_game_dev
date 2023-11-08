class PosicaoNaoVaziaException(Exception):
    def __init__(self):
        super().__init__("A embarcacao nao pode ser posicionada em uma opsicao jah ocupada!")
