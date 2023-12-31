from tela import *
from partida.partida import Partida

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

    def tela_mostra_partida(self, partidas_dict):
        """
        Imprime os dados das partidas.
        """

        contador = 1
        mensagem = ""
        layout = []
        for partida in partidas_dict:
            id = partida["id"]
            data = partida["data"]
            jogador = partida["jogador"]
            vencedor = partida["vencedor"]
            mensagem = f"{contador}: Partida número {id} jogada na data {data}\nJogador: {jogador} com vencedor {vencedor}\n\n"
            contador += 1
            layout_msg_button = [sg.Text(mensagem), sg.Button('Deletar', key=f'delete {id}')]
            layout.append(layout_msg_button)

        layout.append([sg.Button("Retornar", key='0', size=40)])

        window = sg.Window('Lista de partidas', layout, element_justification='c', finalize=True)
        button, _ = window.Read()
        window.close()

        if button == '0':
            return '0'

        if button.startswith('delete'):
            _, opcao = button.split()
            return opcao

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
    
    def desiste_pergunta(self) -> bool:
        """
        Pede confirmacao do usuário.
        """

        sg.ChangeLookAndFeel('Black')

        layout= [
            [sg.Text(f'Deseja realmente desistir da partida?')],
            [sg.Button(' ', size=(0,1), button_color=('white', 'Black'), visible=False)],
            [sg.Button('Sim', key = '0', button_color=('white', 'Black')),
            sg.Text('', size=(10,0)),
            sg.Button('Não', key = '1', button_color=('white', 'Black'))]
        ]

        window = sg.Window('Desistir',  element_justification='c').Layout(layout)
        button, values = window.Read()
        window.close()
        return int(button)

    def espera_interacao(self) -> None:
        """
        Espera o usuario interagir.
        """
        input("Aperte Enter para continuar!")
