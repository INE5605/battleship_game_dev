class Controlador:
    def __init__(self):
        self.__mantem_tela_aberta = True

    @property
    def mantem_tela_aberta(self):
        return self.__mantem_tela_aberta

    @mantem_tela_aberta.setter
    def mantem_tela_aberta(self,mantem_tela_aberta):
        self.__mantem_tela_aberta = mantem_tela_aberta

    def inicializa(self):
        self.mantem_tela_aberta = True
        self.abre_tela()

    def finaliza(self):
        self.mantem_tela_aberta = False