from tela import *

class TelaPartida(Tela):
    def __init__(self):
        super().__init__()

    def tela_principal(self):
        sg.ChangeLookAndFeel('Black')

        ocean_nothing = './imagens/ocean_nothing_80x80.png'
        size = (80,80)

        layout= [
            [sg.Text(' ', size=(20,1))],
            [sg.Image('./imagens/battleship_novo_jogo_tela_partida_main.png',
                      expand_x=True, expand_y=True )],
            [sg.Button(' ', button_color=('white', 'Black'), visible=False)],
            [sg.Button('Novo jogador', key = '1', button_color=('white', 'Black'))],
            [sg.Button('Carregar jogador', key = '2', button_color=('white', 'Black'))],
            [sg.Button('Voltar', key = '0', button_color=('white', 'Black'))],
        ]

        window = sg.Window('Tela Inicial', element_justification='c').Layout(layout)
        button, values = window.Read()
        window.close()
        return int(button), values

    def tela_jogada(self):
        sg.ChangeLookAndFeel('Black')

        layout= [
            [sg.Text(' ', size=(20,1))],
            [sg.Image('./imagens/battleship_novo_jogo_tela_partida_main.png',
                      expand_x=True, expand_y=True )],
            [sg.Button(' ', button_color=('white', 'Black'), visible=False)],
            [sg.Button('Bombardear', key = '1', button_color=('white', 'Black'))],
            [sg.Button('Desistir', key = '0', button_color=('white', 'Black'))],
        ]

        window = sg.Window('Tela Jogada',  element_justification='c').Layout(layout)
        button, values = window.Read()
        window.close()
        return button, values

    def tela_opcoes_mostra_partida(self):

        print("--- Histórico de partidas ---")
        print("Escolha a opcao")
        print("1 - Listar partidas")
        print("0 - Voltar")

        opcoes_validas = [0, 1]

        while True:
            try:
                opcao = int(input("Escolha a opcao: "))
                if opcao not in opcoes_validas:
                    raise ValueError(
                        "Opção inválida, digite uma opção válida."
                    )
                return opcao
            except ValueError:
                print("Digite apenas o numero da opção escolhida.")

    def tela_opcoes_escolhe_partida(self, opcoes_validas_str: str):

        print("--- Histórico de partidas ---")
        print("Escolha uma partida")

        opcoes_validas = range(int(opcoes_validas_str) + 1)

        while True:
            try:
                opcao = int(input("Escolha a opcao: "))
                if opcao not in opcoes_validas:
                    raise ValueError(
                        "Opção inválida, digite uma opção válida."
                    )
                return opcao
            except ValueError:
                print("Digite apenas o numero da opção escolhida.")

    def mostra_partidas(self, numero: int, nome_jogador: str,
                       data: str, terminou: str, desistiu: str,
                       vencedor: str) -> None:
        """
        Imprime dados de uma única partida
        """

        print(f"{numero}: Nome: {nome_jogador}  Data: {data}  Terminou: {terminou}")
        print(f"Desistiu: {desistiu}  Vencedor: {vencedor}")

    def mostra_movimentos(self, numero: str, coord_x: str, coord_y: str,
                       acertou: str, afundou: str) -> None:
        """
        Imprime dados de uma única partida
        """

        print(f"{numero}: Coord: ({coord_x}, {coord_y})  Acertou: {acertou}  Afundou: {afundou}")

    def imprime_mensagem(self, mensagem: str) -> None:
        """
        Imprime mensagem generica
        """
        print(mensagem)

    def confirma_jogador(self, mensagem: str) -> bool:
        """
        Pede confirmacao do usuário.
        """

        resposta = input(
            mensagem
        ).upper()
        return resposta == 'S'

    def espera_interacao(self) -> None:
        """
        Espera o usuario interagir.
        """
        input("Aperte Enter para continuar!")
