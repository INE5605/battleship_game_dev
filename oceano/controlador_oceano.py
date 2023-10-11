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
    Cadastra dimensao do oceano
    Preenche o oceano do computador com embarcacoes
    3 botes (1 posicao)
    2 submarinos (2 posicoes)
    2 fragatas (3 posicoes)
    1 porta avioes (4 posicoes)
    Pede para o usuario preencher as posicoes de suas embarcacoes
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

    def __cadastra_embarcoes_jogador(self):
        self.__preencher_porta_avioes_usuario()

    """
    Chama a tela para definir a direcao da embarcacao
    @Return True se for horizontal, False para vertical
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
            horizontal = self.pede_sera_horizontal()
            
            self.tela_oceano.imprime_mensagem(
                "Entre com os dados de posicao inicial do seu porta aviao:"
            )
            try:
                dados_posicao = self.tela_oceano.pega_posicao()
                posicao_x = int(dados_posicao["posicao_x"])
                posicao_y = int(dados_posicao["posicao_y"])
            except ValueError:
                self.tela_oceano.imprime_mensagem(
                    "Os dados de posicao nao sao numeros inteiros!"
                )

    """
    Preenche o Oceano do computador com embarcacoes
    Posicoes e direcoes aleatorias
    """
    def __preencher_oceano_computador(self):
        self.__add_porta_avioes_computador()
        for _ in range(2):
            self.__add_fragata_computador()
        for _ in range(3):
            self.__add_submarino_computador()
        for _ in range(4):
            self.__add_bote_computador()
            pass

    def __add_fragata_computador():
        is_horizontal = (True, False)[randint(0, 1)]
        fragata = Fragata(is_horizontal)

        if is_horizontal:
            pass
            

    """
    Adiciona porta avioes ao oceano do computador
    Preenche aleatoriamente
    """
    def __add_porta_avioes_computador(self):
        oceano_computador = self.__oceano_computador
        is_horizontal = (True, False)[randint(0, 1) == 0]
        porta_avioes = PortaAvioes(is_horizontal)
        tamanho_oceano_x = self.__oceano_computador.dimensao_x
        tamanho_oceano_y = self.__oceano_computador.dimensao_y

        if is_horizontal:
            while True:
                posicao_y = randint(0, tamanho_oceano_y)
                posicao_x0 = randint(0, tamanho_oceano_x)
                posicao_x1 = posicao_x0 + 1
                posicao_x2 = posicao_x1 + 1
                posicao_x3 = posicao_x3 + 1

                posicoes = [
                    [posicao_x0, posicao_y],
                    [posicao_x1, posicao_y],
                    [posicao_x2, posicao_y],
                    [posicao_x3, posicao_y]
                ]

                for posicao in posicoes:
                    if oceano_computador.verifica_posicao_nao_vazia(
                        posicao[0], posicao[1]
                    ):
                        break
                else:
                    oceano_computador.posicionar_embarcacao(
                        posicoes,
                        porta_avioes
                    )
                    return
        else:
            while True:
                posicao_x = randint(0, tamanho_oceano_x)
                posicao_y0 = randint(0, tamanho_oceano_y)
                posicao_y1 = posicao_y0 + 1
                posicao_y2 = posicao_y1 + 1
                posicao_y3 = posicao_y2 + 1
                
                posicoes = [
                    [posicao_x, posicao_y0],
                    [posicao_x, posicao_y1],
                    [posicao_x, posicao_y2],
                    [posicao_x, posicao_y3]
                ]