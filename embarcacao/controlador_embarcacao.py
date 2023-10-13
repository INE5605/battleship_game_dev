from embarcacao.embarcacao import Embarcacao
from embarcacao.tela_embarcacao import TelaEmbarcacao
from embarcacao.tipos.bote import Bote
from embarcacao.tipos.submarino import Submarino
from embarcacao.tipos.fragata import Fragata
from embarcacao.tipos.porta_avioes import PortaAvioes
from embarcacao.tela_embarcacao import TelaEmbarcacao

class ControladorEmbarcacao:
    def __init__(self, controlador_principal):
        self.__tela_embarcacao = TelaEmbarcacao()
        self.__controlador_principal = controlador_principal
        self.__embarcacoes = []

    @property
    def embarcacoes(self):
        return self.__embarcacoes
    
    def abre_tela(self):
        '''Para desenvolvedores: Abre tela de opções para adicionar embarcações'''

        menu = {
            1: lambda: Bote(),
            2: lambda: Submarino(),
            3: lambda: Fragata(),
            4: lambda: PortaAvioes(),
            0: self.retorna
        }

        opcao = self.__tela_embarcacao.tela_opcoes()
        embarcacao = menu[opcao]()
        print(embarcacao)
        self.retorna()

        self.__embarcacoes.append(embarcacao)
        return embarcacao

    def criar_embarcacoes(self, type: str):
        '''Cria embarcação a partir do parâmetro type\n
        type: {"bote", "submarino", "fragata" ou "portaavioes"}'''

        try:
            if type in ["bote", "submarino", "fragata", "porta_avioes"]:
                menu = {
                    "bote": Bote(),
                    "submarino": Submarino(),
                    "fragata": Fragata(),
                    "porta_avioes": PortaAvioes(),
                }

        except ValueError:
            print('type must be "bote", "submarino", "fragata" or "porta_avioes"')

        embarcacao = menu[type]
        self.__embarcacoes.append(embarcacao)
        print(f"Criando embarcação do tipo {type}.")
        return embarcacao

    def verifica_afundamento(self, embarcacao: Embarcacao) -> bool:
        '''Verifica se embarcação foi afundada type\n
        Retorna True se embarcação foi afundada'''

        return embarcacao.afundou()

    def retorna(self):
        '''Retorna para tela principal'''

        self.__controlador_principal.abre_tela()