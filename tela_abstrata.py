import PySimpleGUI as sg
from abc import abstractmethod

class TelaAbstrata:
    @abstractmethod
    def __init__(self):
        self.__window = None
        self.init_components()

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, window):
        self.__window = window

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass
    
    @abstractmethod
    def hide(self):
        pass

    @abstractmethod
    def unhide(self):
        pass

    @abstractmethod
    def show_message(self, title: str, message: str):
        pass

    @abstractmethod
    def init_components(self):
        pass