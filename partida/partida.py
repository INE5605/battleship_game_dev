class Partida:
    def __init__(self, jogador, oceano_jogador, oceano_computador):
        self.__jogador = jogador
        self.__oceano_jogador = oceano_jogador
        self.__oceano_computador = oceano_computador
        self.__ponto_partida = 0
        self.__historico = list

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
    def ponto_partida(self):
        return self.__ponto_partida
    
    @property
    def historico(self):
        return self.__historico
    
    def adicionar_jogada(self,jogada:dict):
        return self.__historico.append(jogada)