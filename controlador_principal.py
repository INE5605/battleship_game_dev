from embarcacao.controlador_embarcacao import ControladorEmbarcacao
from jogador.controlador_jogador import CtrlJogador as ControladorJogador
from oceano.controlador_oceano import CtrlOceano as ControladorOceano
from partida.controlador_partida import ControladorPartida
from tela_principal import TelaPrincipal
from controlador import Controlador

class ControladorPrincipal(Controlador):
    def __init__(self):
        super().__init__()
        self.tela_principal = TelaPrincipal()
        self.controlador_jogador = ControladorJogador(self)
        self.controlador_embarcacao = ControladorEmbarcacao(self)
        self.controlador_oceano = ControladorOceano(self)
        self.controlador_partida = ControladorPartida(self)

    def abre_tela(self):
        menu = {
            1: self.novo_jogo,
            2: self.jogadores,
            3: self.historico,
            0: self.encerra_jogo
        }

        while self.mantem_tela_aberta:
            opcao, _ = self.tela_principal.tela_opcoes()
            menu[opcao]()

    def novo_jogo(self):
        self.controlador_partida.abre_tela()
    
    def jogadores(self):
        self.controlador_jogador.abre_tela()
    
    def historico(self):
        self.controlador_partida.abre_tela_mostra_partidas()

    def encerra_jogo(self):
        raise SystemExit()
