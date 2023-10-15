from partida.partida import Partida
from partida.tela_partida import TelaPartida

class ControladorPartida:
    def __init__(self, controlador_principal):
        self.tela_partida = TelaPartida()
        self.controlador_principal = controlador_principal
        self.__partida = None

    def abre_tela(self):
        '''Abre tela com opção de novo jogador ou carregando jogador'''

        menu = {
            1: self.novo_jogador_inicia_jogo,
            2: self.carrega_jogador_inicia_jogo,
            0: self.retorna
        }
        
        opcao = self.tela_partida.tela_opcoes()
        menu[opcao]()
        self.abre_tela()

    def abre_tela_partida(self):
        '''Abre tela partida que irá iniciar partida'''
                
        menu = {
            1: lambda: print("\nBombardear computador\n"),
            0: lambda: print("\nDesistir\n"),
        }
        
        opcao = self.tela_partida.tela_opcoes_tela_partida()
        menu[opcao]()
        self.abre_tela_partida()

    def novo_jogador_inicia_jogo(self):
        jogador = self.controlador_principal.controlador_jogador.cadastra_jogador()
        self.inicia_jogo(jogador)

    def carrega_jogador_inicia_jogo(self):
        jogador = self.controlador_principal.controlador_jogador.carrega_jogador()
        self.inicia_jogo(jogador)

    def inicia_jogo(self, jogador):
        
        oceano = self.controlador_principal.controlador_oceano.cadastra_oceano()
        oceano_jogador = oceano.oceano_jogador
        oceano_computador = oceano.oceano_computador
        partida = self.cria_partida(jogador, oceano_jogador, oceano_computador)
        self.__partida = partida
        self.abre_tela_partida()

    def adiciona_embarcacoes_jogador_oceano(self):
        '''Cria ambos oceanos e adiciona cada embarcacao no oceano'''

        self.controlador_principal.controlador_oceano.cadastra_oceano()
        pass

    def adiciona_embarcacoes_computador_oceano(self):
        '''Cria ambos oceanos e adiciona cada embarcacao no oceano'''

        self.controlador_principal.controlador_oceano.cadastra_oceano()
        pass

    def cria_partida(self, jogador_1, oceano_1, oceano_2):
        '''Cria uma partida'''
        return Partida()

    def bombardeia_computador(self):
        '''Bombardeia inimigo'''
        pass

    def verifica_resposta(self, entrada, if_true = lambda: None,
                          if_false = lambda: None):
        '''Verifica resposta do usuário. Segundo parâmetro define
        o que fazer se verdadeiro e segundo parâmetro define o que fazer se falso'''

        try:
            if entrada in ["s", "n"]:
                if entrada == "s":
                    if_true
                else:
                    if_false

        except ValueError:
            print('argument given is not aceptable. Please write either "s" or "n"')

    def retorna(self):
        '''Retorna para a tela inicial do jogo'''
        self.controlador_principal.abre_tela()
