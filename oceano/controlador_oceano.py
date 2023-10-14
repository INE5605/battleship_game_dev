from embarcacao.embarcacao import Embarcacao
from oceano.oceano import Oceano
from oceano.tela_oceano import TelaOceano
from random import randint


class CtrlOceano:
    def __init__(self, controlador_principal) -> None:
        self.controlador_principal = controlador_principal
        self.tela_oceano = TelaOceano()
        self.__oceano_jogador = None
        self.__oceano_computador = None

    @property
    def oceano_jogador(self) -> Oceano:
        return self.__oceano_jogador

    @oceano_jogador.setter
    def oceano_jogador(self, oceano_jogador) -> None:
        self.__oceano_jogador = oceano_jogador

    def cadastra_oceano(self) -> None:
        """
        Cadastra dimensao do oceano.
        Preeenche o oceano do computador:\n
        3 botes (1 posicao);\n
        2 submarinos (2 posicoes);\n
        2 fragatas (3 posicoes);\n
        1 porta avioes (4 posicoes);\n
        Pede para o usuario preencher as posicoes das suas embarcacoes.
        """
        while True:
            dados_oceanos = self.tela_oceano.cadastra_oceano()
            try:
                dimensao_x = int(dados_oceanos["dimensao_x"])
                dimensao_y = int(dados_oceanos["dimensao_y"])
            except ValueError:
                self.tela_oceano.imprime_mensagem(
                    "As dimensoes do oceano devem ser numeros inteiros!"
                )
            else:
                oceano_jogador = Oceano(
                    dimensao_x,
                    dimensao_y
                )
                oceano_computador = Oceano(
                    dimensao_x,
                    dimensao_y
                )
                self.oceano_jogador = oceano_jogador
                self.__oceano_computador = oceano_computador
                self.tela_oceano.imprime_mensagem(
                    f"Oceano de dimensao x: {dimensao_x} e " +
                    f"dimensao y: {dimensao_y} " +
                    "cadastrado com sucesso!"
                )
                self.__preencher_oceano_computador()
                self.tela_oceano.imprime_mensagem(
                    "-- Cadastro das embarcacoes do Jogador --"
                )
                self.__cadastra_embarcoes_jogador()

    def pede_sera_horizontal(self) -> bool:
        """
        Define a direcao da embarcacao do jogador.
        @Return -> True se horizontal, False se vertical.
        """
        while True:
            try:
                horizontal = self.tela_oceano.pega_direcao_embarcacao_horizontal()
            except ValueError:
                self.tela_oceano.imprime_mensagem("A sua resposta deve ser 'S' OU 'N'!")
            else:
                return horizontal


    def preencher_embarcacao_usuario(
        self,
        embarcacoes: list
    ):
        """
        Preenche posicoes do oceano do usuario com embarcacoes.
        """
        for embarcacao in embarcacoes:
            while True:
                try:
                    dados_posicao = self.tela_oceano.pega_posicao()
                    is_horizontal = self.tela_oceano.pega_direcao_embarcacao_horizontal()
                    posicoes = self.__gera_posicoes_complementares(
                        embarcacao,
                        dados_posicao,
                        is_horizontal
                    )
                    adicionou = self.__checa_posicao_adiciona_se_vazio(
                        posicoes,
                        self.oceano_jogador,
                    )
                    if adicionou:
                        break
                except ValueError:
                    self.tela_oceano.imprime_mensagem(
                        "Os dados de posicao nao sao numeros inteiros!"
                    )
                except IndexError:
                    self.tela_oceano.imprime_mensagem(
                        "A posicao final indicada eh maior do que a posicao do oceano"
                    )

    def __preencher_oceano_computador(self) -> None:
        """
        Preenche o Oceano do computador com as 8 embarcacoes aleatorias.
        """
        quantidades = {
            "bote": 3,
            "fragata": 2,
            "submarino": 2,
            "porta_avioes": 1
        }

        for tipo, quantidade in quantidades.items():
            for _ in range(quantidade):
                embarcacao = self.controlador_principal.controlador_embarcacao.criar_embarcacoes(tipo)
                self.__add_embarcacao_computador(embarcacao, self.__sera_horizontal())

    def __add_embarcacao_computador(
        self,
        embarcacao: Embarcacao
    ):
        """
        Adiciona uma embarcacao do computador em seu oceano.
        """
        while True:
            posicoes: list = self.__gera_posicoes_embarcacao(
                embarcacao
            )

            adicionou = self.__checa_posicao_adiciona_se_vazio(
                posicoes,
                self.__oceano_computador,
                embarcacao
            )

            if adicionou:
                break

    def __sera_horizontal(self):
        """
        Define a direcao de uma embarcacao aleatoriamente
        """
        is_horizontal = (True, False)[randint(0, 1) == 0]
        return is_horizontal

    def __checa_posicao_adiciona_se_vazio(
        self,
        posicoes: list,
        oceano: Oceano,
        embarcacao: Embarcacao
    ):
        """
        Se as posicoes estiverem desocupadas preenche com a embarcacao
        @return -> true se adicionou, false se nao estava com posicoes vazias
        """
        for posicao in posicoes:
            if oceano.verifica_posicao_nao_vazia(
                posicao[0],
                posicao[1]
            ):
                break
        else:
            oceano.posicionar_embarcacao(
                posicoes,
                embarcacao
            )
            return True
        return False

    def __gera_posicoes_embarcacao(
        self,
        embarcacao: Embarcacao,
        is_horizontal: bool
    ) -> list:
        """
        Gera e retorna as posicoes de uma embarcacao com base em posicao e tamanho
        """
        posicoes = []
        posicao_y = randint(
            0, self.__oceano_computador.dimensao_y - 1
        )
        posicao_x = randint(
            0, self.__oceano_computador.dimensao_x - 1
        )

        if is_horizontal:
            for i in range(0, embarcacao.tamanho):
                posicoes.append(
                    [posicao_x - i, posicao_y]
                )
        else:
            # vertical:
            for i in range(0, embarcacao.tamanho):
                posicoes.append(
                    [posicao_x, posicao_y - i]
                )

        return posicoes

    def __gera_posicoes_complementares(
        self,
        embarcacao: Embarcacao,
        dados_posicao: dict,
        is_horizontal: bool
    ) -> list:
        """
        Gera as posicoes da embarcacao com base no tamanho da embarcacao
        Definido pela posicao final que o usuario escolheu
        @return -> lista de inteiros com as posicoes no formato:
        [posicao_x, posicao_y]
        """
        posicao_x0 = int(dados_posicao["posicao_x"])
        posicao_y0 = int(dados_posicao["posicao_y"])
        posicoes = [
            [posicao_x0, posicao_y0],
        ]
        for i in range(1, embarcacao.tamanho):
            if is_horizontal:
                posicao_x = posicao_x0 - i
                posicoes.append(posicao_x, posicao_y0)
            else:
                # vertical
                posicao_y = posicao_y0 - i
                posicoes.append(posicao_x0, posicao_y)

        return posicoes
