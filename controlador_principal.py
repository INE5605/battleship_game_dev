from embarcacao.controlador_embarcacao import ControladorEmbarcacao
from jogador.controlador_jogador import CtrlJogador as ControladorJogador
from oceano.controlador_oceano import CtrlOceano as ControladorOceano
from partida.controlador_partida import ControladorPartida
from tela_principal import TelaPrincipal

class ControladorPrincipal:
    def __init__(self):
        self.tela_principal = TelaPrincipal()
        self.controlador_jogador = ControladorJogador(self)
        self.controlador_embarcacao = ControladorEmbarcacao(self)
        self.controlador_oceano = ControladorOceano(self)
        self.controlador_partida = ControladorPartida(self)

        self.abre_tela()

    def abre_tela(self):
        menu = {
            1: self.controlador_jogador.abre_tela,
            2: self.controlador_partida.abre_tela,
            0: self.encerra_jogo
        }
        
        opcao = self.tela_principal.tela_opcoes()
        menu[opcao]()
        self.retorna()

    def retorna(self):
        self.__controlador_principal.abre_tela()
        
    def encerra_jogo(self):
        print("Fechando jogo")
        raise SystemExit()