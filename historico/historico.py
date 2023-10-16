class Historico:
    def __init__(self, data, jogador):
        self.__data = data
        self.__jogador = jogador
        self.__vitoria = False
        self.__movimentos = []

    @property
    def jogador(self):
        return self.__jogador
    
    @property
    def data(self):
        return self.__data
    
    @property
    def vitoria(self):
        return self.__vitoria
    
    @property
    def movimentos(self):
        return self.__movimentos


    def adiciona_movimentos(self, movimentos):
        for movimento in movimentos:
            self.__movimentos.append(movimento)    

    def define_vitoria(self):
        self.__vitoria = True
