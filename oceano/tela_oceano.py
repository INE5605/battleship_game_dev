from embarcacao.embarcacao import Embarcacao
from embarcacao.tipos.bote import Bote
from embarcacao.tipos.fragata import Fragata
from embarcacao.tipos.porta_avioes import PortaAvioes
from embarcacao.tipos.submarino import Submarino


class TelaOceano:
    def cadastra_oceano(self) -> dict:
        """
        @return -> dicionario com chave dimensao_x e dimensao_y
        com os valores de tamanho do oceano, definido pelo usuario
        """
        while True:
            try:
                dimensao_x = int(input("Entre com a dimensao X do oceano: "))
                dimensao_y = int(input("Entre com a dimensao Y do oceano: "))
                return {
                    "dimensao_x": dimensao_x,
                    "dimensao_y": dimensao_y
                }
            except ValueError:
                print("Entre apenas com numeros inteiros!")

    def imprime_mensagem(self, mensagem: str) -> None:
        """
        Imprime mensagem generica
        """
        print(mensagem)

    def espera_interacao(self) -> None:
        """
        Espera o usuario interagir com tecla 'Enter'
        """
        input("Aperte enter para continuar!")


    def pega_posicao(self, embarcacao: Embarcacao) -> dict:
        """
        Pede ao usuario a posicao e retorna em um dicionario
        com as chaves "posicao_x" e "posicao_y"
        """
        if isinstance(embarcacao, Bote):
            print("Cadastro da posicao final do BOTE!")
        elif isinstance(embarcacao, Fragata):
            print("Cadastro da posicao final da FRAGATA!")
        elif isinstance(embarcacao, PortaAvioes):
            print("Cadastro da posicao final do PORTA AVIOES!")
        elif isinstance(embarcacao, Submarino):
            print("Cadastro da posicao final do SUBMARINO!")
        while True:
            try:
                posicao_x = int(input("Posicao X: "))
                posicao_y = int(input("Posicao Y: "))
            except ValueError:
                print(
                    "A posicao da embarcacao aceita apenas numeros inteiros"
                )
            else:
                return {
                    "posicao_x": posicao_x,
                    "posicao_y": posicao_y
                }


    def pega_direcao_embarcacao_horizontal(self) -> bool:
        """
        Pede ao usuario se a embarcacao sera Horizontal
        @return -> true (horizontal)
        @return -> false (vertical)
        """
        while True:
            horizontal = input("Sua embarcacao sera horizontal [S/N]? ").upper()
            try:
                if horizontal != 'S' and horizontal != 'N':
                    raise ValueError
            except:
                print("A sua resposta deve ser 'S' ou 'N'!")
            else:
                return horizontal == 'S'
            
    def mostra_oceano_escondido(self, oceano):
        '''Mostra oceano refêrencia para jogador'''

        cont = 0
        linha_um = [str(x) for x in range(len(oceano))]

        linha_um = '  '.join(linha_um)

        linha_um_str = ''
        for string in linha_um.split():
            if string in ['0','1','2','3','4','5','6','7','8','9']:
                linha_um_str += string + '  '
            else:
                linha_um_str += string + ' '

        print(' x ', linha_um_str)
        print('y')

        for linha in oceano:    

            linha = '  '.join(linha)
            if cont < 10:
                print(cont , " " , linha)
            else:
                print(cont, "", linha)
            cont+=1
