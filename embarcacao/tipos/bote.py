from embarcacao.embarcacao import Embarcacao

class Bote(Embarcacao):
    def __init__(self, id, tamanho = 1, letra = "B"):
        super().__init__(id, tamanho, letra)

    def possiveis_sprites(self, horizontal) -> list:
        if horizontal:
            sprites = ['./imagens/bote_h']
        else:
            sprites = ['./imagens/bote_v']

        return sprites