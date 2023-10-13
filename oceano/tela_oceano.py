class TelaOceano:
    def cadastra_oceano(self) -> dict:
        while True:
            try:
                dimensao_x = int(input("Entre com a dimensao X do oceano"))
                dimensao_y = int(input("Entre com a dimensao Y do oceano"))
                return {
                    "dimensao_x": dimensao_x,
                    "dimensao_y": dimensao_y
                }
            except ValueError:
                print("Entre apenas com numeros inteiros!")

    def imprime_mensagem(self, mensagem: str) -> None:
        print(mensagem)

    def espera_interacao(self) -> None:
        input("Aperte enter para continuar!")

    def pega_posicao(self) -> dict:
        while True:
            try:
                posicao_x = int(input("Posicao X:"))
                posicao_y = int(input("Posicao Y:"))
                return {
                    "posicao_x": posicao_x,
                    "posicao_y": posicao_y
                }
            except ValueError:
                print(
                    "A posicao da embarcacao aceita apenas numeros inteiros"
                )

    def pega_direcao_embarcacao_horizontal(self) -> bool:
        while True:
            horizontal = input("Sua embarcacao sera horizontal [S/N]? ").upper()
            try:
                if horizontal != 'S' and horizontal != 'N':
                    raise ValueError
            except:
                print("A sua resposta deve ser 'S' ou 'N'!")
            return horizontal
