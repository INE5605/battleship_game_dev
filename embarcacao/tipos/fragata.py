from embarcacao.embarcacao import Embarcacao

class Fragata(Embarcacao):
    def __init__(self, id, tamanho = 3, letra = "F"):
        super().__init__(id, tamanho, letra)

    def possiveis_sprites(self, horizontal) -> list:
        if horizontal:
            sprites = ['./imagens/fragata_1_h',
                    './imagens/fragata_2_h',
                    './imagens/fragata_3_h']
        
        else:
            sprites = ['./imagens/fragata_1_v',
                    './imagens/fragata_2_v',
                    './imagens/fragata_3_v']

        return sprites
