from embarcacao.embarcacao import Embarcacao


class Oceano:
    def __init__(self, dimensao_x: int, dimensao_y: int) -> None:
        self.__dimensao_x: int = int(dimensao_x)
        self.__dimensao_y: int = int(dimensao_y)
        self.__campo: list = []
        self.__embarcacoes: list = []
        self.escondido: list = []

        for _ in range(self.__dimensao_x):
            coluna = []
            for _ in range(self.__dimensao_y):
                coluna.append(' ')
            self.__campo.append(coluna)

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
    Verifica se a posicao recebida NAO esta vazia
    (vazio = ' ')
    @return true se nao haver nenhuma embarcacao na posicao
    @return false se a posicao estiver ocupada
    """
    def verifica_posicao_nao_vazia(
        self, posicao_x: int, posicao_y: int
    ) -> bool:
        """Verifica se na posição (x,y) existe um valor
        não vazio. Retorna True se uma
        das posições for negativa"""

        if self.campo[posicao_x][posicao_y] == ' ':
            return False
        return True
    
    def verifica_posicao_negativa(
            self, posicao_x: int, posicao_y: int
            ) -> bool:
        """Verifica se a posição x ou posição
        y é maior é maior ou igual que zero. Retorna True se uma
        das posições for positiva"""

        if posicao_x >=0 and posicao_y >= 0:
            return False
        return True

    def posicionar_embarcacao(
        self,
        posicoes: list,
        embarcacao: Embarcacao
    ) -> None:
        """
        posicoes: lista de posicoes com: [posicao_x, posicao_y]
        define o valor do campo para a posicao com a embarcacao
        """
        for posicao in posicoes:
            x = posicao[0]
            y = posicao[1]

            if self.verifica_posicao_nao_vazia(x, y):
                raise Exception

            if isinstance(embarcacao, Embarcacao):
                self.campo[x][y] = embarcacao
                self.__embarcacoes.append(embarcacao)

    def edita_oceano_escondido(self, coord_x, coord_y, value):
        self.escondido[coord_y][coord_x] = value
