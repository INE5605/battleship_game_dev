from tela_abstrata import *

class TelaPartidaPrincipal(TelaAbstrata):
    def __init__(self):
        super().__init__()

    def open(self):
        self.init_components()
        event, values = self.__window.Read()

        if event is None or event == sg.WIN_CLOSED:
            pass

        self.__window.close()
        return event, values

    def hide(self):
        self.__window.Hide()

    def unhide(self):
        self.__window.UnHide()

    def close(self):
        self.__window.Close()

    def show_message(self, title: str, message: str):
        sg.Popup(title, message)

    def init_components(self):
        sg.ChangeLookAndFeel('Black')

        ocean_nothing = './imagens/ocean_nothing_80x80.png'
        size = (80,80)

        layout= [
            [sg.Text(' ', size=(20,1))],
            [sg.Image('./imagens/battleship_novo_jogo_tela_partida_main.png',
                      expand_x=True, expand_y=True )],
            [sg.Button(' ', button_color=('white', 'Black'), visible=False)],
            [sg.Button('Novo jogador', button_color=('white', 'Black'))],
            [sg.Button('Carregar jogador', button_color=('white', 'Black'))],
            [sg.Button('Voltar', button_color=('white', 'Black'))],
        ]

        self.__window = sg.Window('Tela Inicial', element_justification='c').Layout(layout)
        self.__window.Finalize()
