from partida.partida import Partida
from partida.tela_partida import TelaPartida
from jogador.jogador import Jogador
from oceano.oceano import Oceano

class ControladorPartida:
    def __init__(self, controlador_principal):
        self.tela_partida = TelaPartida()
        self.controlador_principal = controlador_principal
        self.__partida = []
        self.vencedor = None

    @property
    def partida(self) -> [Partida]:
        return self.__partida

    def partida_atual(self) -> Partida:
        '''Chama última partida registrada
        
        @return -> Partida'''

        return self.partida[-1]
    
    def mostra_partidas(self):
        '''Mostra partidas'''

        for partida in self.partida():
            self.tela_partida.imprime_mensagem((partida))
        self.tela_partida.mostra_e_escolhe_partida()


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
            1: self.inicia_bombardeios,
            0: self.retorna,
        }

        opcao = self.tela_partida.tela_opcoes_tela_partida()
        menu[opcao]()

    def novo_jogador_inicia_jogo(self):
        '''Cria um novo jogador que depois será usado para uma nova partida'''

        jogador = self.controlador_principal.controlador_jogador.cadastra_jogador()
        self.inicia_jogo(jogador)

    def carrega_jogador_inicia_jogo(self, jogador: Jogador = None):
        '''Carrega um jogador da lista de jogadores salvos.
        Tal jogador será depois usado para uma nova partida'''

        if jogador == None:
            jogador = self.controlador_principal.controlador_jogador.carrega_jogador()
        self.inicia_jogo(jogador)

    def inicia_jogo(self, jogador):
        '''Inicia partida'''

        oceano_jogador, oceano_computador = self.cadastra_oceanos()
        self.cadastra_partida(jogador, oceano_jogador, oceano_computador)
        self.jogadas()

    def cadastra_oceanos(self):
        '''Cadastra tanto o oceano que será usado
        pelo jogador quanto o oceano que será usado
        pelo computador
        
        @return -> oceano_jogador: Oceano, oceano_computador: Oceano'''

        oceano_jogador, oceano_computador = self.controlador_principal.controlador_oceano.cadastra_oceano()

        return oceano_jogador, oceano_computador

    def cadastra_partida(self, jogador, oceano_jogador, oceano_computador):
        '''Cadastra partida e adiciona a lista de partidas
        @return -> Partida se argumentos or None'''

        if (isinstance(jogador, Jogador) and
            isinstance(oceano_jogador, Oceano) and
            isinstance(oceano_computador, Oceano)):

            partida = Partida(jogador, oceano_jogador, oceano_computador)
            self.partida.append(partida)
            return partida

        return None

    def jogadas(self):
        '''Mostra oceanos escondidos e inicia partida.
        Enquanto a partida não termina e o jogador não desiste,
        a tela partida será chamada para que uma nova jogada seja feita'''

        while not self.partida_atual().terminou or not self.partida_atual().desistiu:
            if self.vencedor != None:
                self.tela_partida.imprime_mensagem(
                    f"{self.vencedor} venceu a partida!")
                break
            self.mostra_ambos_oceanos_escondidos()
            self.abre_tela_partida()

        self.controlador_principal.abre_tela()

    def inicia_bombardeios(self):
        '''Bombardeia computador e é bombardeado pelo computador'''

        jogada = self.bombardeia('computador', self.partida_atual().oceano_computador)
        self.partida_atual().adiciona_jogada(jogada["jogadas"])
        self.partida_atual().jogador.incrementa_score(jogada["pontos_ganhos"])

        jogada = self.bombardeia('jogador', self.partida_atual().oceano_jogador)
        self.partida_atual().incrementa_pontos_computador = jogada["pontos_ganhos"]

    def bombardeia(self, quem: str, oceano: Oceano):
        '''Bombardeia oponente ou é bombardeado pelo oponente
        @param: quem -> "computador", caso queira bombardear
        o computador ou "jogador", caso queria ser bombardeado
        pelo computador

        @return -> Só Deus sabe
        '''

        return self.controlador_principal.controlador_oceano.bombardeia_oceano(
            bombardeia_quem = quem,
            oceano = oceano)

    def mostra_ambos_oceanos_escondidos(self):
        '''Mostra ambos oceanos como uma matriz com o
        mínimo de informação necessária para o jogador.'''

        self.tela_partida.imprime_mensagem("\n\nSuas embarcações:\n")
        self.mostra_oceano_escondido(
            self.partida_atual().oceano_jogador.escondido)

        self.tela_partida.imprime_mensagem("\nEmbarcações do seu oponente:\n")
        self.mostra_oceano_escondido(
            self.partida_atual().oceano_computador.escondido)
        
    
    def mostra_oceano_escondido(self, oceano):
        '''Mostra um único oceano escondido.'''

        self.controlador_principal.controlador_oceano.tela_oceano.mostra_oceano_escondido(
                oceano)

    def verifica_resposta(self, entrada, if_true = lambda: None,
                          if_false = lambda: None):
        '''Verifica resposta do usuário.
        Segundo parâmetro define o que fazer se verdadeiro
        e segundo parâmetro define o que fazer se falso'''

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

        if self.tela_partida.confirma_jogador("Tem certeza que deseja desistir? [S/N]"):
            self.controlador_principal.abre_tela()
        else:
            self.abre_tela_partida()
