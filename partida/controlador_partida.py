from partida.partida import Partida
from partida.tela_partida import TelaPartida
from jogador.jogador import Jogador
from oceano.oceano import Oceano

class ControladorPartida:
    def __init__(self, controlador_principal):
        self.tela_partida = TelaPartida()
        self.controlador_principal = controlador_principal
        self.__partida = None
        self.vencedor = None

    @property
    def partida(self) -> Partida:
        return self.__partida

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
            1: self.bombardeia_computador,
            0: self.retorna,
        }
        
        opcao = self.tela_partida.tela_opcoes_tela_partida()
        menu[opcao]()

    def novo_jogador_inicia_jogo(self):
        jogador = self.controlador_principal.controlador_jogador.cadastra_jogador()
        self.inicia_jogo(jogador)
 
    def carrega_jogador_inicia_jogo(self):
        jogador = self.controlador_principal.controlador_jogador.carrega_jogador()
        self.inicia_jogo(jogador)

    def inicia_jogo(self, jogador):
        '''Inicia partida'''
        
        oceano_jogador, oceano_computador = self.controlador_principal.controlador_oceano.cadastra_oceano()
        partida = self.cria_partida(jogador, oceano_jogador, oceano_computador)
        self.__partida = partida

        terminou = False
        desistiu = False
        while not self.partida.terminou or not self.partida.desistiu:
            if self.vencedor != None:
                self.tela_partida.imprime_mensagem(
                    f"{self.vencedor} venceu a partida!"
                )
                break
            self.tela_partida.imprime_mensagem("\n\nSuas embarcações:\n")
            self.controlador_principal.controlador_oceano.tela_oceano.mostra_oceano_escondido(
                oceano_jogador.escondido)

            self.tela_partida.imprime_mensagem("\nEmbarcações do seu oponente:\n")
            self.controlador_principal.controlador_oceano.tela_oceano.mostra_oceano_escondido(
                oceano_computador.escondido)
            
            self.abre_tela_partida()
        self.controlador_principal.abre_tela()

    def cria_partida(self, jogador, oceano_jogador, oceano_computador):
        '''Cria uma partida
        @return Partida (if arguments are right) or None'''

        if (isinstance(jogador, Jogador) and
            isinstance(oceano_jogador, Oceano) and
            isinstance(oceano_computador, Oceano)):
            return Partida(jogador, oceano_jogador, oceano_computador)
        
        return None

    def bombardeia_computador(self):
        '''Bombardeia computador e é bombardeado pelo computador'''
        jogada = self.controlador_principal.controlador_oceano.bombardeia_oceano(
            bombardeia_quem = 'computador',
            oceano = self.partida.oceano_computador)
        self.partida.adiciona_jogada(jogada["jogadas"])
        self.partida.jogador.incrementa_score(jogada["pontos_ganhos"])

        jogada = self.controlador_principal.controlador_oceano.bombardeia_oceano(
            bombardeia_quem = 'jogador',
            oceano = self.__partida.oceano_jogador)
        self.partida.incrementa_pontos_computador = jogada["pontos_ganhos"]
        

    def verifica_resposta(self, entrada, if_true = lambda: None,
                          if_false = lambda: None):
        '''Verifica resposta do usuário. Segundo parâmetro define
        o que fazer se verdadeiro e segundo parâmetro define o que fazer se falso'''

        try:
            if entrada in ["s", "n", "S", "N"]:
                if entrada == "s" or "S":
                    if_true()
                else:
                    if_false()

        except ValueError:
            self.tela_partida.imprime_mensagem(
                "argument given is not aceptable. Please write either 's' or 'n'")

    def retorna(self) -> None:
        '''Retorna para a tela inicial do jogo'''
        self.controlador_principal.abre_tela()
