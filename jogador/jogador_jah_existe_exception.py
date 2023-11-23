class JogadorJahExisteException(Exception):
    def __init__(self) -> None:
        super().__init__("Já existe um jogador com esse nome!")
