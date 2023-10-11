from embarcacao.embarcacao import Embarcacao
from embarcacao.tipos.fragata import Fragata
from embarcacao.tipos.bote import Bote
from embarcacao.tipos.porta_avioes import PortaAvioes
from embarcacao.tipos.submarino import Submarino


class Oceano:
    def __init__(self, dimensao_x: int, dimensao_y: int) -> None:
        self.__dimensao_x: int = int(dimensao_x)
        self.__dimensao_y: int = int(dimensao_y)
        self.__campo: list = []
        self.__dados_embarcacoes: list = []

        for _ in range(self.__dimensao_x):
            coluna = []
            for _ in range(self.__dimensao_y):
                coluna.append('X')
        self.__campo.append([coluna])

    @property
    def dimensao_x(self) -> int:
        return self.__dimensao_x

    @property
    def dimensao_y(self) -> int:
        return self.__dimensao_y

    @property
    def campo(self) -> list:
        return self.__campo

    @property
    def dados_embarcacoes(self) -> list:
        return self.__dados_embarcacoes

    """
    Verifica se a posicao recebida esta vazia (vazio = ' ')
    @return true se nao haver nenhuma embarcacao na posicao
    @return false se a posicao estiver ocupada
    """
    def verifica_posicao_nao_vazia(
        self, posicao_x: int, posicao_y: int
    ) -> bool:
        if self.campo[posicao_x][posicao_y] == ' ':
            return False
        return True

    """
    posicoes: lista de posicoes com: [posicao_x, posicao_y]
    define o valor do campo para a posicao
    F para Fragata
    B para Bote
    P para porta avioes
    S para submarino
    """
    def posicionar_embarcacao(
        self,
        posicoes: list, 
        embarcacao: Embarcacao
    ) -> None:
        for posicao in posicoes:
            x = posicao[0]
            y = posicao[1]
            
            if self.verifica_posicao_nao_vazia(x, y):
                raise Exception

            if isinstance(embarcacao, Fragata):
                self.campo[x][y] = "F"
            elif isinstance(embarcacao, Bote):
                self.campo[x][y] = "B"
            elif isinstance(embarcacao, PortaAvioes):
                self.campo[x][y] = "P"
            elif isinstance(embarcacao, Submarino):
                self.campo[x][y] = "S"
