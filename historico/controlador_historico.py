from historico.historico import Historico
from historico.tela_historico import TelaHistorico
from jogador.jogador import Jogador
from datetime import datetime
class ControladorHistorico:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_historico = TelaHistorico()
        self.__historicos = []

    def inicia_historico(self, jogador):
        data_atual = datetime.now().strftime("%d/%m/%Y")
        historico = Historico(data_atual, jogador)
        self.__historicos.append(historico)

        return historico
    
    def adiciona_movimentos(self, movimentos):
        self.__historicos[-1].adiciona_movimentos(movimentos)
        print(self.__historicos[0].data)

    def busca_historico_por_jogador(self, jogador):
        historicos_do_jogador = []
        for historico in self.__historicos:
            if historico.jogador.nome == jogador.nome:
               historicos_do_jogador.append(historico)
        return historicos_do_jogador
    
    def abre_tela(self):
        jogador = self.__controlador_principal.controlador_jogador.lista_jogador_por_score()
        historico_do_jogador = self.busca_historico_por_jogador(jogador)
        self.exibe_historicos(historico_do_jogador)

    def exibe_historicos(self, historicos):
        numero = self.__tela_historico.pega_historico(historicos)
        historico_escolhido = historicos[numero]
        self.__tela_historico.exibe_movimentos(historico_escolhido)

