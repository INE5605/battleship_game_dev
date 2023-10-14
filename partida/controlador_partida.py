from partida.partida import Partida
from partida.tela_partida import TelaPartida

class ControladorPartida:
    def __init__(self, controlador_principal):
        self.__tela_partida = TelaPartida()
        self.__controlador_principal = controlador_principal
        self.__partida = None

    def abre_tela(self):
        '''Abre tela com opção de novo jogador ou carregando jogador'''

        menu = {
            1: self.inicia_novo_jogo,
            2: lambda: print("\nCarregar jogador ainda não implementado\n"),
            0: self.retorna
        }
        
        opcao = self.__tela_partida.tela_opcoes_tela_novo_jogo()
        menu[opcao]()
        self.abre_tela()

    def abre_tela_partida(self):
        '''Abre tela partida que irá iniciar partida'''
                
        menu = {
            1: lambda: print("\nBombardear computador\n"),
            0: lambda: print("\nDesistir\n"),
        }
        
        opcao = self.__tela_partida.tela_opcoes_tela_partida()
        menu[opcao]()
        self.abre_tela_partida()

    def inicia_novo_jogo(self):
        '''Inicia jogo a partir de um novo jogador'''

        jogador = self.__controlador_principal.__controlador_jogador.cadastra_jogador() #Trocar abre_tela por abre_tela_novo_jogo
        
        self.cria_embarcacoes()
        self.adiciona_embarcacoes_no_oceano()
        partida = self.cria_partida()
        self.__partida = partida
        self.abre_tela_partida()

    def cria_embarcacoes(self):
        '''Adiciona 3 botes, 2 submarinos, 2 fragatas e 1 porta aviões'''

        mapa = {"bote":3,
               "submarino":2,
               "fragata":2,
               "porta_avioes":1}

        for tipo_de_embarcacao, quantidade in mapa.items():
            for _ in range(quantidade):
                self.__controlador_principal.controlador_embarcacao.criar_embarcacoes(tipo_de_embarcacao)

    def adiciona_embarcacoes_no_oceano(self):
        '''Cria ambos oceanos e adiciona cada embarcacao no oceano'''
        self.__controlador_principal.controlador_oceano.cadastra_oceano
        pass

    def cria_partida(self, jogador_1, jogador_2, oceano_1, oceano_2):
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
        self.__controlador_principal.abre_tela()