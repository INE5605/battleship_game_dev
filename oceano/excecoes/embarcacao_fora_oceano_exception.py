class EmbarcacaoForaOceanoException(Exception):
    def __init__(self) -> None:
        super().__init__(
            "A sua embarcação não foi posicionada em uma posição válida!\n > Tente posicionar novamente!"
        )
