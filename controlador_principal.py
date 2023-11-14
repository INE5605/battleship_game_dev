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

    def abre_tela(self):
        menu = {
            'Novo jogo': self.controlador_partida.abre_tela,
            'Jogadores': self.controlador_jogador.abre_tela,
            'Histórico': self.controlador_partida.abre_tela_mostra_historico,
            'Sair': self.encerra_jogo
        }

        botao, _ = self.tela_principal.open()
        if botao != None:
            menu[botao]()
        self.abre_tela()

    def encerra_jogo(self):
        raise SystemExit()
