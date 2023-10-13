from embarcacao.embarcacao import Embarcacao
from embarcacao.tipos.bote import Bote
from embarcacao.tipos.fragata import Fragata
from embarcacao.tipos.porta_avioes import PortaAvioes
from embarcacao.tipos.submarino import Submarino
from oceano.oceano import Oceano
from oceano.tela_oceano import TelaOceano
from random import randint


class CtrlOceano:
    def __init__(self, controlador_principal) -> None:
        self.__controlador_principal = controlador_principal
        self.__tela_oceano = TelaOceano()
        self.__oceano_jogador = None
        self.__oceano_computador = None

    @property
    def oceano_jogador(self) -> Oceano:
        return self.__oceano_jogador

    @oceano_jogador.setter
    def oceano_jogador(self, oceano_jogador) -> None:
        self.__oceano_jogador = oceano_jogador

    @property
    def tela_oceano(self) -> TelaOceano:
        return self.__tela_oceano

    """
    Cadastra dimensao do oceano preenchendo o oceano do computador
    3 botes (1 posicao), 2 submarinos (2 posicoes), 2 fragatas (3 posicoes)
    1 porta avioes (4 posicoes).
    Pede para o usuario preencher as posicoes das suas embarcacoes
    """
    def cadastra_oceano(self) -> None:
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

    """
    Cadastro das embarcacoes do jogador
    """
    def __cadastra_embarcoes_jogador(self) -> None:
        self.tela_oceano.pega_posicao
        self.__preencher_embarcacao_usuario()

    """
    Define a direcao da embarcacao
    @Return True se horizontal, False se vertical
    """
    def pede_sera_horizontal(self) -> bool:
        while True:
            try:
                horizontal = self.tela_oceano.pega_direcao_embarcacao_horizontal()
            except ValueError:
                self.tela_oceano.imprime_mensagem("A sua resposta deve ser 'S' OU 'N'!")
            else:
                return horizontal

    """
    Preenche posicao do oceano com porta aviao
    """
    def __preencher_embarcacao_usuario(self):
        while True:
            is_horizontal = self.pede_sera_horizontal()
            porta_aviao = PortaAvioes(is_horizontal)
            self.tela_oceano.imprime_mensagem(
                "Entre com os dados de posicao final do seu porta aviao:"
            )
            try:
                dados_posicao = self.tela_oceano.pega_posicao()
                posicoes = self.__gera_posicoes_complementares(
                    porta_aviao,
                    dados_posicao
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

    """
    Preenche o Oceano do computador com as 8 embarcacoes aleatorias
    """
    def __preencher_oceano_computador(self):
        porta_aviao = PortaAvioes(self.__sera_horizontal())
        self.__add_embarcacao_computador(porta_aviao)
        
        for _ in range(2):
            fragata = Fragata(self.__sera_horizontal())
            self.__add_embarcacao_computador(fragata)
            
            submarino = Submarino(self.__sera_horizontal())
            self.__add_embarcacao_computador(submarino)

        for _ in range(4):
            bote = Bote(self.__sera_horizontal())
            self.__add_embarcacao_computador(bote)

    """
    Adiciona uma embarcacao do computador
    """
    def __add_embarcacao_computador(
        self,
        embarcacao: Embarcacao
    ):
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

    """
    Define a direcao de uma embarcacao aleatoriamente
    """
    def __sera_horizontal(self):
        is_horizontal = (True, False)[randint(0, 1) == 0]
        return is_horizontal

    """
    Se as posicoes estiverem desocupadas preenche com a embarcacao
    @return true se adicionou, false se nao estava com posicoes vazias
    """
    def __checa_posicao_adiciona_se_vazio(
        self,
        posicoes: list,
        oceano: Oceano,
        embarcacao: Embarcacao
    ):
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

    """
    gera e retorna as posicoes de uma embarcacao com base em posicao e tamanho
    """
    def __gera_posicoes_embarcacao(
        self,
        embarcacao: Embarcacao,
    ) -> list:
        posicoes = []
        posicao_y = randint(
            0, self.__oceano_computador.dimensao_y - 1
        )
        posicao_x = randint(
            0, self.__oceano_computador.dimensao_x - 1
        )

        if embarcacao.is_horizontal:
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
        dados_posicao: dict
    ) -> list:
        posicao_x0 = int(dados_posicao["posicao_x"])
        posicao_y0 = int(dados_posicao["posicao_y"])
        posicoes = [
            [posicao_x0, posicao_y0],
        ]
        for i in range(1, embarcacao.tamanho):
            if embarcacao.is_horizontal:
                posicao_x = posicao_x0 - i
                posicoes.append(posicao_x, posicao_y0)
            else:
                # vertical
                posicao_y = posicao_y0 - i
                posicoes.append(posicao_x0, posicao_y)

        return posicoes
