from embarcacao.embarcacao import Embarcacao
from embarcacao.tela_embarcacao import TelaEmbarcacao
from embarcacao.tipos.bote import Bote
from embarcacao.tipos.submarino import Submarino
from embarcacao.tipos.fragata import Fragata
from embarcacao.tipos.porta_avioes import PortaAvioes
from embarcacao.tela_embarcacao import TelaEmbarcacao

class ControladorEmbarcacao:
    def __init__(self, controlador_principal):
        self.tela_embarcacao = TelaEmbarcacao()
        self.controlador_principal = controlador_principal
        self.__embarcacoes = []
        self.__proximo_id = 0

    @property
    def embarcacoes(self):
        return self.__embarcacoes
    
    @property
    def proximo_id(self):
        return self.__proximo_id
    
    def pega_embarcacao(self, id):
        for embarcacao in self.embarcacoes:
            if embarcacao.id == id:
                return embarcacao
        
        return None

    def criar_embarcacoes(self, type: str) -> Embarcacao:
        '''Cria embarcação a partir do parâmetro type\n
        type: {"bote", "submarino", "fragata" ou "portaavioes"}
        
        @return -> Bote(), Submarino(), Fragata() ou PortaAvioes()'''

        try:
            if type in ["bote", "submarino", "fragata", "porta_avioes"]:
                menu = {
                    "bote": Bote(self.proximo_id),
                    "submarino": Submarino(self.proximo_id),
                    "fragata": Fragata(self.proximo_id),
                    "porta_avioes": PortaAvioes(self.proximo_id),
                }

        except ValueError:
            print('type must be "bote", "submarino", "fragata" or "porta_avioes"')

        embarcacao = menu[type]
        self.__embarcacoes.append(embarcacao)
        self.__proximo_id += 1
        return embarcacao

    def verifica_afundamento(self, embarcacao: Embarcacao) -> bool:
        '''Verifica se embarcação foi afundada type\n
        Retorna True se embarcação foi afundada'''

        return embarcacao.afundou(self)

    def edita_posicoes_e_sprites(self, embarcacao: Embarcacao, posicoes:list, horizontal: bool):
        '''Edita posições dentro do oceano, inclue direção da embarcação e inclui sprites'''

        self.adiciona_posicoes(embarcacao, posicoes)
        self.edita_horizontal(embarcacao, horizontal)
        self.adiciona_sprites(embarcacao, horizontal)

    def edita_horizontal(self, embarcacao: Embarcacao, horizontal: bool):
        '''Define uma embarcacao como horizontal (bool)'''

        embarcacao.horizontal = horizontal

    def adiciona_posicoes(self, embarcacao: Embarcacao, posicoes: list):
        '''Adiciona posições do oceano em que a embarcação foi instanciada'''

        embarcacao.adiciona_posicoes(posicoes)

    def adiciona_sprites(self, embarcacao, horizontal):
        sprites = embarcacao.possiveis_sprites(horizontal)
        for sprite in sprites:
            embarcacao.sprites.append(sprite)
