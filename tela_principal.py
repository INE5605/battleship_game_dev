from tela import *

class TelaPrincipal(Tela):
    def __init__(self):
        super().__init__()
        self.init_components()

    @property
    def window(self):
        return self.__window
    
    @window.setter
    def window (self, window):
        self.__window = window

    def tela_opcoes(self):
        sg.ChangeLookAndFeel('Black')
        layout= [
            [sg.Text(' ', size=(20,1))],
            [sg.Image('./imagens/battleship_main_w_text.png',
                      expand_x=True, expand_y=True )],
            [sg.Button(' ', button_color=('white', 'Black'), visible=False)],
            [sg.Button('Novo jogo', key = "1", button_color=('white', 'Black'))],
            [sg.Button('Jogadores', key = "2", button_color=('white', 'Black'))],
            [sg.Button('Históricos', key = "3", button_color=('white', 'Black'))],
            [sg.Button('Sair', key = "0", button_color=('white', 'Black'))],
        ]

        window = sg.Window('Tela Inicial',  element_justification='c').Layout(layout)
        button, values = window.Read()
        window.close()
        return int(button), values

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def hide(self):
        self.__window.Hide()

    def unhide(self):
        self.__window.UnHide()

    def show_message(self, title: str, message: str):
        sg.Popup(title, message)
