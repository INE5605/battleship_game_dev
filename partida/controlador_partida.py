from partida.partida import Partida
from partida.tela_partida import TelaPartida
from jogador.jogador import Jogador
from oceano.oceano import Oceano
from controlador import Controlador
from partida.partida_dao import PartidaDAO


class ControladorPartida(Controlador):
    def __init__(self, controlador_principal):
        super().__init__()
        self.tela_partida = TelaPartida()
        self.controlador_principal = controlador_principal
        self.__partida_dao = PartidaDAO()
        self.vencedor = None
        self.__numero_partidas = len(self.__partida_dao.get_all())

    @property
    def partidas(self) -> dict:
        return self.__partida_dao.get_all()

    def partida_atual(self) -> Partida:
        '''Chama última partida registrada

        @return -> Partida'''

        return self.__partida_dao.get(self.__numero_partidas)

    def abre_tela(self):
        '''Abre tela com opção de novo jogador ou carregando jogador'''

        menu = {
            1: self.novo_jogador_inicia_jogo,
            2: self.carrega_jogador_inicia_jogo,
            0: self.retorna
        }

        while self.mantem_tela_aberta:
            opcao, _ = self.tela_partida.tela_principal()
            menu[opcao]()

    def abre_tela_mostra_partidas(self):
        """
        Lista todos as partidas cadastradas.
        """
        if len(self.partidas) == 0:
            self.tela_partida.escreve_mensagem(
                "Não há partidas no sistema!", "Lista de partidas"
            )
        else:
            partidas = []
            for partida in self.partidas:
                partida_dicionario = {
                    "id": partida.id,
                    "data": partida.data,
                    "jogador": partida.jogador,
                    "vencedor": partida.vencedor
                }
                partidas.append(partida_dicionario)
            opcao = self.tela_partida.tela_mostra_partida(partidas)

        if opcao != '0':
                self.remove_partida(int(opcao))

    def remove_partida(self, id_partida:int):
        """
        Remove partida pelo id
        """

        self.__partida_dao.remove(id_partida)
        self.tela_partida.escreve_mensagem("Partida removida")

    def mostra_movimentos(self, partida):
        '''Mostra movimentos.'''

        cont = 0
        for movimento in partida.movimentos:
            cont += 1
            movimento = movimento[0]

            self.tela_partida.mostra_movimentos(str(cont),
                                                str(movimento['coord_x']), str(movimento['coord_y']),
                                                str(movimento['acertou']), str(movimento['afundou']))

        self.tela_partida.imprime_mensagem("")
        self.retorna_tela_historicos_partida

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
            self.__numero_partidas += 1
            id = self.__numero_partidas
            partida = Partida(jogador, oceano_jogador, oceano_computador, id)
            self.__partida_dao.add(partida)
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
            self.inicia_bombardeios()

        self.controlador_principal.abre_tela()

    def inicia_bombardeios(self):
        '''Bombardeia computador e é bombardeado pelo computador'''

        jogada = self.bombardeia('computador', self.partida_atual().oceano_jogador, self.partida_atual().oceano_computador)
        self.partida_atual().adiciona_jogada(jogada["jogadas"])
        self.partida_atual().jogador.incrementa_score(jogada["pontos_ganhos"])

        self.controlador_principal.controlador_jogador.jogador_dao.salvar()

        jogada = self.bombardeia('jogador', self.partida_atual().oceano_jogador, self.partida_atual().oceano_computador)
        self.partida_atual().incrementa_pontos_computador = jogada["pontos_ganhos"]

    def bombardeia(self, quem: str, oceano_jogador: Oceano, oceano_computador: Oceano):
        '''Bombardeia oponente ou é bombardeado pelo oponente.

        @param: quem -> "computador", caso queira bombardear
        o computador ou "jogador", caso queria ser bombardeado
        pelo computador.
        '''

        return self.controlador_principal.controlador_oceano.bombardeia_oceano(bombardeia_quem = quem,
            oceano_jogador = oceano_jogador,
            oceano_computador = oceano_computador)   

    def retorna(self) -> None:
        '''Retorna para a tela inicial do jogo.'''

        self.controlador_principal.abre_tela()

    def desiste_pergunta(self) -> None:
        '''Desiste da partida e retorna para a tela inicial do jogo.'''

        menu = {
            1: self.inicia_bombardeios,
            0: self.retorna,
        }

        opcao = self.tela_partida.desiste_pergunta()
        menu[opcao]()
