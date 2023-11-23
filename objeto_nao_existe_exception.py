class ObjetoNaoExisteException(Exception):
    def __init__(self) -> None:
        super().__init__("Objeto não encontrado na base de dados")
