from embarcacao.embarcacao import Embarcacao
from embarcacao.tipos.bote import Bote
from embarcacao.tipos.fragata import Fragata
from embarcacao.tipos.porta_avioes import PortaAvioes
from embarcacao.tipos.submarino import Submarino
from tela import *

class TelaOceano(Tela):
    def __init__(self):
        super().__init__()

    def cadastra_oceano(self) -> dict:
        """
        @return -> dicionario com chave dimensao_x e dimensao_y
        com os valores de tamanho do oceano, definido pelo usuario
        """

        sg.ChangeLookAndFeel('Black')

        ocean_nothing = './imagens/ocean_nothing_80x80.png'
        size = (80,80)

        layout= [
            [sg.Text(' ', size=(20,1))],
            [sg.Image('./imagens/battleship_novo_jogo_tela_partida_main.png',
                      expand_x=True, expand_y=True )],
            [sg.Text("Digite a dimensão x,y do oceano:"),
            sg.Input("8", key="dimensao_x", size=2),
            sg.Text("x"),
            sg.Input("8", key="dimensao_y", size=2)],
            [sg.Button('Continuar', key = '1', button_color=('white', 'Black')),
            sg.Button('Voltar', key = '0', button_color=('white', 'Black'))],
            [sg.Button('Enter', visible=False, bind_return_key=True)]
        ]

        window = sg.Window('Tela Inicial', element_justification='c').Layout(layout)

        while True:
            event, values = window.Read()
            if event in (None, 'Exit'):
                break
            try:
                if (int(values['dimensao_x']) > 5 and
                    int(values['dimensao_y']) > 5):

                    window.close()
                    return  {
                            "dimensao_x": values['dimensao_x'],
                            "dimensao_y": values['dimensao_y']
                        }
                else:
                    self.escreve_mensagem("Data invalida! Número menor que 5!")
            except ValueError:
                    self.escreve_mensagem("Data invalida! Digite apenas números inteiros maiores que 5!")

    def imprime_mensagem(self, mensagem: str) -> None:
        """
        Imprime mensagem generica
        """

        print(mensagem)

    def espera_interacao(self) -> None:
        """
        Espera o usuario interagir com tecla 'Enter'
        """

        input("Aperte enter para continuar!")


    def pega_posicao(self, embarcacao: Embarcacao, max_dimensao_x, max_dimensao_y) -> dict:
        """
        Pede ao usuario a posicao e retorna em um dicionario
        com as chaves "posicao_x" e "posicao_y"
        """
        if isinstance(embarcacao, Bote):
            print("Cadastro da posicao final do BOTE!")
        elif isinstance(embarcacao, Fragata):
            print("Cadastro da posicao final da FRAGATA!")
        elif isinstance(embarcacao, PortaAvioes):
            print("Cadastro da posicao final do PORTA AVIOES!")
        elif isinstance(embarcacao, Submarino):
            print("Cadastro da posicao final do SUBMARINO!")
        while True:
            try:
                print("\nPosicionando embarcação\n")

                posicao_x = int(input("Posicao X: "))
                posicao_y = int(input("Posicao Y: "))
            except ValueError:
                print(
                    "A posicao da embarcacao aceita apenas numeros inteiros"
                )
            else:
                if (posicao_x >= 0 and posicao_x <= max_dimensao_x and
                        posicao_y >= 0 and posicao_y <= max_dimensao_y):
                    return {
                        "posicao_x": posicao_x,
                        "posicao_y": posicao_y
                    }
                else:
                    print("Posição x ou posição y inválida")

    def retorna_posicoes_embarcacao(self, max_dimensao_x, max_dimensao_y) -> dict:
        """
        @return -> dicionario com chave coordenada_x e coordenada_y
        com as coordenadas x e y, definidas pelo usuario
        """

        while True:
            try:
                while True:
                    print("Dimensões para bombardeio:\n")
                    dimensao_x = int(input("Entre com dimensao X: "))
                    dimensao_y = int(input("Entre com a dimensao Y: "))
                    if (dimensao_x >= 0 and dimensao_x <= max_dimensao_x and
                        dimensao_y >= 0 and dimensao_y <= max_dimensao_y):
                        return {
                            "dimensao_x": dimensao_x,
                            "dimensao_y": dimensao_y
                        }
                    print("Dimensão x ou y inválida. Verifique por favor\n")
            except ValueError:
                print("Entre apenas com numeros inteiros!")

    def pega_direcao_embarcacao_horizontal(self) -> bool:
        """
        Pede ao usuario se a embarcacao sera Horizontal
        @return -> true (horizontal)
        @return -> false (vertical)
        """

        while True:
            horizontal = input("Sua embarcacao sera horizontal [S/N]? ").upper()
            try:
                if horizontal != 'S' and horizontal != 'N':
                    raise ValueError
            except:
                print("A sua resposta deve ser 'S' ou 'N'!")
            else:
                return horizontal == 'S'
            
    def mostra_oceano_escondido(self, oceano):
        '''Mostra oceano refêrencia para jogador'''

        cont = 0
        linha_um = [str(x) for x in range(len(oceano))]

        linha_um = '  '.join(linha_um)

        linha_um_str = ''
        for string in linha_um.split():
            if string in ['0','1','2','3','4','5','6','7','8','9']:
                linha_um_str += string + '  '
            else:
                linha_um_str += string + ' '

        print(' x ', linha_um_str)
        print('y')

        for linha in oceano:    

            linha = '  '.join(linha)
            if cont < 10:
                print(cont , " " , linha)
            else:
                print(cont, "", linha)
            cont+=1
