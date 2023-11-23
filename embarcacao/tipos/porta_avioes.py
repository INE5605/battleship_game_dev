from embarcacao.embarcacao import Embarcacao

class PortaAvioes(Embarcacao):
    def __init__(self, id, tamanho = 4, letra = 'P'):
        super().__init__(id, tamanho, letra)

    def possiveis_sprites(self, horizontal) -> list:
        if horizontal:
            sprites = ['./imagens/porta_avioes_1_h',
                    './imagens/porta_avioes_2_h',
                    './imagens/porta_avioes_3_h',
                    './imagens/porta_avioes_4_h']
        
        else:
            sprites = ['./imagens/porta_avioes_1_v',
                    './imagens/porta_avioes_2_v',
                    './imagens/porta_avioes_3_v',
                    './imagens/porta_avioes_4_v']

        return sprites
