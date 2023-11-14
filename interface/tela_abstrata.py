import PySimpleGUI as sg
from abc import abstractmethod


class TelaAbstrata:
    def __init__(self):
        self.__window = None
        self.inicializar_componentes()

    def fechar(self):
        self.__window.Close()

    def imprime_mensagem(self, mensagem: str):
        sg.Popup(mensagem)
