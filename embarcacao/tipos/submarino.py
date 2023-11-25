from embarcacao.embarcacao import Embarcacao

class Submarino(Embarcacao):
    def __init__(self, id, tamanho = 2, letra = 'S'):
        super().__init__(id, tamanho, letra)

    def possiveis_sprites(self, horizontal) -> list:
        if horizontal:
            sprites = ['./imagens/submarino_1_h',
                    './imagens/submarino_2_h']
        
        else:
            sprites = ['./imagens/submarino_1_v',
                    './imagens/submarino_2_v']

        return sprites
