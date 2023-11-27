from embarcacao.embarcacao import Embarcacao
from embarcacao.tipos.bote import Bote
from embarcacao.tipos.fragata import Fragata
from embarcacao.tipos.porta_avioes import PortaAvioes
from embarcacao.tipos.submarino import Submarino
from oceano.oceano import Oceano
from copy import deepcopy
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
                    self.escreve_mensagem("Data inválida! Número menor que 6!")
            except ValueError:
                    self.escreve_mensagem("Data inválida! Digite apenas números inteiros maiores que 5!")

    def imprime_mensagem(self, mensagem: str) -> None:
        """
        Imprime mensagem generica
        """

        print(mensagem)

    def implementa_layout_dedicado_embarcacao(self, embarcacao):

        size = (50, 50)
        bg_color = ('LightBlue4')
        pad = (1,1)

        if isinstance(embarcacao, Bote):
            mensagem_1 = [sg.Text('Cadastro da posicao do bote.')]
            layout_sprite = [sg.Image('./imagens/bote_h.png', background_color=bg_color, size=size, pad=pad)]

        elif isinstance(embarcacao, Submarino):
            mensagem_1 = [sg.Text('Cadastro da posição do submarino.')]
            layout_sprite = [sg.Image('./imagens/submarino_1_h.png', background_color=bg_color, size=(50, 50), pad=pad),
               sg.Image('./imagens/submarino_2_h.png', background_color=bg_color, size=(50, 50), pad=pad)]

        elif isinstance(embarcacao, Fragata):
            mensagem_1 = [sg.Text('Cadastro da posição da fragata.')]
            layout_sprite = [sg.Image('./imagens/fragata_1_h.png', background_color=bg_color, size=(50, 50), pad=pad),
               sg.Image('./imagens/fragata_2_h.png', background_color=bg_color, size=(50, 50), pad=pad),
               sg.Image('./imagens/fragata_3_h.png', background_color=bg_color, size=(50, 50), pad=pad)]

        elif isinstance(embarcacao, PortaAvioes):
            mensagem_1 = [sg.Text('Cadastro da posicao final do porta-aviões.')]
            layout_sprite = [sg.Image('./imagens/porta_avioes_1_h.png', background_color=bg_color, size=(50, 50), pad=pad),
                      sg.Image('./imagens/porta_avioes_2_h.png', background_color=bg_color, size=(50, 50), pad=pad),
                      sg.Image('./imagens/porta_avioes_3_h.png', background_color=bg_color, size=(50, 50), pad=pad),
                      sg.Image('./imagens/porta_avioes_4_h.png', background_color=bg_color, size=(50, 50), pad=pad)]

        return mensagem_1, layout_sprite

    def pega_posicao_para_preencher_embarcacao(self, oceano_jogador: Oceano, embarcacao: Embarcacao) -> dict:
        """
        Pede ao usuario a posicao e retorna em um dicionario
        com as chaves "posicao_x" e "posicao_y"
        """

        mensagem_1, layout_sprite = self.implementa_layout_dedicado_embarcacao(embarcacao)

        sg.ChangeLookAndFeel('Black')

        checkbox_layout = [sg.Radio('Horizontal', "RADIO1", key="horizontal", default=True, size=(10,1)),
                           sg.Radio('Vertical', "RADIO1", key = "vertical")]

        while True:
            layout_1 = deepcopy(oceano_jogador.layout)

            layout_2 = [mensagem_1,
                        layout_sprite,
                        checkbox_layout
                        ]

            layout = [
                [sg.Text('Insira uma embarcação')],
                [sg.Text('Clique em um espaço para definir a posição da embarcação')],
                [sg.Frame(layout=layout_1, title='Oceano',title_color='white', relief=sg.RELIEF_SUNKEN),
                sg.Frame(layout=layout_2, title='Infos',title_color='white', relief=sg.RELIEF_SUNKEN)]
                ]

            window = sg.Window('Battleship', layout, element_justification='c', finalize=True)

            event, values = window.Read()

            window.close()
 
            _, posicao_x, posicao_y = event.split()

            return {
                "posicao_x": int(posicao_x),
                "posicao_y": int(posicao_y),
                "horizontal": values['horizontal']
                    }

    def tela_bombardeia(self, oceano_jogador: Oceano, oceano_computador:Oceano) -> dict:
        """
        Pede ao usuario a posicao e retorna em um dicionario
        com as chaves "posicao_x" e "posicao_y"
        """

        sg.ChangeLookAndFeel('Black')

        while True:
            layout_1 = deepcopy(oceano_computador.escondido_layout)
            layout_2 = deepcopy(oceano_jogador.layout)

            layout = [
                [sg.Text('Derrote seu oponente')],
                [sg.Text('Clique em um campo do inimigo para bombardear')],
                [sg.Frame('Inimigo', layout=layout_1, key = 'Inimigo', title_color='red', relief=sg.RELIEF_SUNKEN),
                sg.Frame('Jogador', layout=layout_2,  key='Jogador', title_color='blue', relief=sg.RELIEF_SUNKEN)],
                [sg.Button('Desistir', key = 'desistir', button_color=('white', 'Black'))]
                ]

            window = sg.Window('Battleship', layout= layout, element_justification='c', finalize=True)

            event, values = window.Read()

            if event == sg.WIN_CLOSED:
                break

            window.close()

            if event.startswith('Frame2') or event == "desistir":
                return event, values
            
            else:
                return None, None

    def escreve_mensagem(self, mensagem: str, titulo = "") -> None:
        """
        Imprime mensagem generica.
        """

        sg.Popup(titulo, mensagem)
