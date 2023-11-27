from embarcacao.embarcacao import Embarcacao
from oceano.excecoes.posicao_nao_vazia_exception import PosicaoNaoVaziaException
import PySimpleGUI as sg

class Oceano:
    def __init__(self, dimensao_x: int, dimensao_y: int, player) -> None:
        self.__player:int = player
        self.__dimensao_x: int = int(dimensao_x)
        self.__dimensao_y: int = int(dimensao_y)
        self.__campo: list = []
        self.__embarcacoes: list = []
        self.__escondido: list = []
        self.__layout: list = []
        self.__escondido_layout: list = []

        for _ in range(self.__dimensao_x):
            coluna = []
            for _ in range(self.__dimensao_y):
                coluna.append(' ')
            self.__campo.append(coluna)

    @property
    def player(self) -> int:
        return self.__player

    @player.setter
    def player(self, player):
        self.__player = player

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
    def embarcacoes(self) -> list:
        return self.__embarcacoes
    
    @property
    def escondido(self) -> list:
        return  self.__escondido
    
    @escondido.setter
    def escondido (self, escondido):
        self.__escondido = escondido

    @property
    def layout(self):
        return self.__layout

    @layout.setter
    def layout (self, layout):
        self.__layout = layout

    @property
    def escondido_layout(self):
        return self.__escondido_layout

    @escondido_layout.setter
    def escondido_layout (self, escondido_layout):
        self.__escondido_layout = escondido_layout

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
        não vazio após verificar se tais posições estão
        dentro da matriz.
         
        @return -> True se uma das posições estiver fora
        da matriz"""

        if not self.verifica_posicao_fora_matriz(posicao_x, posicao_y):
            if self.campo[posicao_y][posicao_x] == ' ':
                return False
        return True
    
    def verifica_posicao_negativa(
            self, posicao_x: int, posicao_y: int
            ) -> bool:
        """Verifica se a posição x ou posição
        y é maior é maior ou igual que zero. Retorna True se uma das posições
        for negativa"""

        if posicao_x >=0 and posicao_y >= 0:
            return False
        return True
    
    def verifica_posicao_fora_matriz(self, posicao_x: int, posicao_y: int
            ) -> bool:
        """Verifica se posição está fora da matriz oceano.
        
        @return -> True se uma das posições estiver fora da matriz"""

        if posicao_x < self.dimensao_x and posicao_y < self.dimensao_y:
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
                raise PosicaoNaoVaziaException()

            if isinstance(embarcacao, Embarcacao):
                self.campo[y][x] = embarcacao
                self.__embarcacoes.append(embarcacao)

    def edita_oceano_escondido(self, coord_x, coord_y, value):
        '''Edita oceano escondido ao receber coordenadas
        e o novo valor de tal coordenada'''

        self.escondido[coord_y][coord_x] = value

    def edita_oceano_layout(self, coord_x, coord_y, value:str):
        '''Edita oceano definido em forma de um layout do PySimpleGui
        ao receber coordenada e o novo valor de tal coordenada
        value deve ser um png por exemplo "./oceano"'''

        new_button = sg.Button(" ", key = f"{coord_x} {coord_y}",
                   button_color=('LightBlue4'), image_filename = value+'.png', image_size=(50, 50),
                   image_subsample=1, border_width=0, pad=(1, 1))

        self.layout[coord_y][coord_x] = new_button

    def edita_oceano_escondido_layout(self, coord_x, coord_y, value):
        '''Edita oceano escondido definido em forma de um layout do PySimpleGui
        ao receber coordenada e o novo valor de tal coordenada
        value deve ser um png por exemplo "./oceano"'''

        new_button = sg.Button(" ", key = f"{coord_x} {coord_y}",
                   button_color=('LightBlue4'), image_filename = value+'.png', image_size=(50, 50),
                   image_subsample=1, border_width=0, pad=(1, 1))

        self.escondido_layout[coord_y][coord_x] = new_button

    def edita_oceano_escondido_layout_afundado(self, coord_x, coord_y, value):
        '''Edita oceano escondido definido em forma de um layout do PySimpleGui
        ao receber coordenada e o novo valor de tal coordenada
        value deve ser um png por exemplo "./oceano"'''

        new_button = sg.Button(" ", key = f"{coord_x} {coord_y}",
                   button_color=('DarkRed'), image_filename = value+'.png', image_size=(50, 50),
                   image_subsample=1, border_width=0, pad=(1, 1))

        self.escondido_layout[coord_y][coord_x] = new_button
