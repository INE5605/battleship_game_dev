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
    def oceano_jogador(self, oceano_jogador):
        self.__oceano_jogador = oceano_jogador

    @property
    def tela_oceano(self):
        return self.__tela_oceano

    """
    Cadastra dimensao do oceano preenchendo o oceano do computador
    3 botes (1 posicao), 2 submarinos (2 posicoes), 2 fragatas (3 posicoes)
    1 porta avioes (4 posicoes).
    Pede para o usuario preencher as posicoes das suas embarcacoes
    """
    def cadastra_oceano(self):
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
    def __cadastra_embarcoes_jogador(self):
        self.__preencher_porta_avioes_usuario()

    """
    Define a direcao da embarcacao
    @Return True se horizontal, False se vertical
    """
    def pede_sera_horizontal(self):
        while True:
            try:
                direcao = self.tela_oceano.pega_direcao_embarcacao()
            except ValueError:
                self.tela_oceano.imprime_mensagem("A sua resposta deve ser 'S' OU 'N'!")
            else:
                return (False, True)[direcao == 'Horizontal']

    """
    Preenche posicao do oceano com porta aviao
    """
    def __preencher_porta_avioes_usuario(self):
        while True:
            is_horizontal = self.pede_sera_horizontal()
            porta_aviao = PortaAvioes(is_horizontal)
            self.tela_oceano.imprime_mensagem(
                "Entre com os dados de posicao inicial do seu porta aviao:"
            )
            try:
                dados_posicao = self.tela_oceano.pega_posicao()
                posicao_x = int(dados_posicao["posicao_x"])
                posicao_y = int(dados_posicao["posicao_y"])
                
                if is_horizontal:
                    posicao_x1 = posicao_x + 1
                    posicao_x2 = posicao_x1 + 1
                    posicao_x3 = posicao_x2 + 1

                    posicoes = [
                        [posicao_x, posicao_y],
                        [posicao_x1, posicao_y],
                        [posicao_x2, posicao_y],
                        [posicao_x3, posicao_y],
                    ]
                    
                    self.__checa_posicao_adiciona_se_vazio(
                        posicoes,
                        self.oceano_jogador,
                        
                    )
                        
            except ValueError:
                self.tela_oceano.imprime_mensagem(
                    "Os dados de posicao nao sao numeros inteiros!"
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
