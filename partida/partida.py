from datetime import datetime as Datetime
from jogador.jogador import Jogador
from oceano.oceano import Oceano

class Partida:
    def __init__(self, jogador: Jogador, oceano_jogador: Oceano, oceano_computador: Oceano):
        self.__data = Datetime.now().strftime("%d/%m/%Y")
        self.__jogador = jogador
        self.__oceano_jogador = oceano_jogador
        self.__oceano_computador = oceano_computador
        self.__ponto_jogador = 0
        self.__ponto_computador = 0
        self.__terminou = False
        self.__desistiu = False
        self.__vencedor = None
        self.__movimentos = []

    @property
    def data(self):
        return self.__data

    @property
    def jogador(self):
        return self.__jogador

    @property
    def oceano_jogador(self):
        return self.__oceano_jogador

    @property
    def oceano_computador(self):
        return self.__oceano_computador

    @property
    def ponto_jogador(self):
        return self.__ponto_jogador

    @property
    def ponto_computador(self):
        return self.__ponto_computador

    @property
    def terminou(self):
        return self.__terminou

    @property
    def desistiu(self):
        return self.__desistiu
    
    @property
    def vencedor(self):
        return self.__vencedor

    @property
    def ponto_computador(self):
        return self.__ponto_computador

    @property
    def movimentos(self):
        return self.__movimentos
    
    def adiciona_jogada(self,jogada:dict):
        return self.__movimentos.append(jogada)
    
    def incrementa_pontos_computador(self, pontos):
        self.ponto_computador += pontos
