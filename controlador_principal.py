from embarcacao.controlador_embarcacao import ControladorEmbarcacao
from jogador.controlador_jogador import CtrlJogador as ControladorJogador
from oceano.controlador_oceano import CtrlOceano as ControladorOceano
from partida.controlador_partida import ControladorPartida
from tela_principal import TelaPrincipal

class ControladorPrincipal:
    def __init__(self):
        self.tela_principal = TelaPrincipal()
        self.__controlador_jogador = ControladorJogador(self)
        self.__controlador_embarcacao = ControladorEmbarcacao(self)
        self.__controlador_oceano = ControladorOceano(self)
        self.__controlador_partida = ControladorPartida(self)

        self.abre_tela()

    def abre_tela(self):
        menu = {
            1: self.__controlador_jogador.abre_tela,
            2: self.__controlador_partida.abre_tela,
            3: self.__controlador_oceano.abre_tela,
            0: self.encerra_jogo
        }
        
        opcao = self.tela_principal.tela_opcoes()
        menu[opcao]()
        self.abre_tela()
        
    def encerra_jogo(self):
        print("Fechando jogo")
        raise SystemExit()