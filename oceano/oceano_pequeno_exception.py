class OceanoPequenoException(Exception):
    def __init__(self) -> None:
        super().__init__("As dimensões do oceano são menores do que o necessário")
