class Partida:
    def __init__(self, jogador, pc, oceano_jogador, oceano_pc):
        self.__jogador = jogador
        self.__pc = pc
        self.__oceano_jogador = oceano_jogador
        self.__oceano_pc = oceano_pc
        self.__ponto_partida = 0
        self.__historico = list(dict())

    @property
    def jogador(self):
        return self.__jogador

    @property
    def pc(self):
        return self.__pc
    
    @property
    def oceano_jogador(self):
        return self.__oceano_jogador
    
    @property
    def oceano_pc(self):
        return self.__oceano_pc
    
    @property
    def ponto_partida(self):
        return self.__ponto_partida
    
    @property
    def historico(self):
        return self.__historico
    
    def adicionar_jogada(self,jogada:dict):
        return self.__historico.append(jogada)