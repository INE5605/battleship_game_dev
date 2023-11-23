class NomeVazioException(Exception):
    def __init__(self) -> None:
        super().__init__("O nome não pode ser vazio!")
