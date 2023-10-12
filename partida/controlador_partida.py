from partida.partida import Partida
from partida.tela_partida import TelaPartida

class ControladorPartida:
    def __init__(self, controlador_principal):
        self.__tela_partida = TelaPartida()
        self.__controlador_principal = controlador_principal

    def abre_tela(self):
        menu = {
            1: self.inicia_novo_jogo,
            2: lambda: print("\nCarregar jogador ainda não implementado\n"),
            0: self.retorna
        }
        
        opcao = self.__tela_partida.tela_opcoes()
        menu[opcao]()
        self.abre_tela()

    
    def inicia_novo_jogo(self):
        '''Inicia jogo a partir de um novo jogador'''

        self.__controlador_principal.controlador_jogador.abre_tela(loop = False)
        jogador = self.__controlador_principal.controlador_jogador.jogadores[0]

        print(f"Você deseja iniciar o jogo com o jogador {jogador.nome}? [s,n]")
        self.verifica_resposta(input(), if_false = self.abre_tela())
        
        self.adicionar_embarcacoes_no_oceano()

    def adicionar_embarcacoes_no_oceano(self):
        mapa = {"bote":3,
               "submarino":2,
               "fragata":2,
               "porta_avioes":1
        }
        for tipo_de_embarcacao, quantidade in mapa.items():
            for _ in range(quantidade):
                self.__controlador_principal.controlador_embarcacao.criar_embarcacoes(tipo_de_embarcacao)

    def verifica_resposta(self, entrada, if_true = lambda: None, if_false = lambda: None):
        '''Verifica resposta do usuário. Segundo parâmetro define o que fazer caso o usuário '''
        try:
            if entrada in ["s", "n"]:
                if entrada == "s":
                    if_true
                else:
                    if_false

        except ValueError:
            print('argument given is not aceptable. Please write either "s" or "n"')


    def retorna(self):
        self.__controlador_principal.abre_tela()