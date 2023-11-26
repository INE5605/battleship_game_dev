import PySimpleGUI as sg
from datetime import datetime
from jogador.jogador import Jogador
from tela import *


class TelaJogador(Tela):
    def __init__(self):
        super().__init__()
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Black')
        layout = [
            [sg.Button("Adicionar um jogador", key="1", size=40)],
            [sg.Button("Alterar um jogador", key="2", size=40)],
            [sg.Button("Listar jogadores", key="3", size=40)],
            [sg.Button("Excluir um jogador", key="4", size=40)],
            [sg.Button("Jogar com um jogador ja cadastrado", key="5", size=40)],
            [sg.Button("Retornar", key="0", size=40)],
        ]
        self.window = sg.Window("Tela do jogador").Layout(layout)

    def tela_opcoes(self) -> int:
        sg.ChangeLookAndFeel('Black')
        layout = [
            [sg.Button("Adicionar um jogador", key="1", size=40)],
            [sg.Button("Alterar um jogador", key="2", size=40)],
            [sg.Button("Listar jogadores", key="3", size=40)],
            [sg.Button("Excluir um jogador", key="4", size=40)],
            [sg.Button("Jogar com um jogador ja cadastrado", key="5", size=40)],
            [sg.Button("Retornar", key="0", size=40)],
        ]

        window = sg.Window("Tela do jogador").Layout(layout)
        button, values = window.Read()
        window.close()
        return int(button)

    def adiciona_jogador(self):
        """
        Adiciona um jogador ao jogo.
        Pede nome e data de nascimento.
        """
        layout = [
            [sg.Text("Digite o seu nome: ")],
            [sg.Input("", key="nome")],
            [sg.Text("Digite a sua data de nascimento (dd/mm/yyyy): ")],
            [sg.Input("", key="data_nasc")],
            [sg.Button("Adicionar", key="1", size=40)],
            [sg.Button("Cancelar", key="0", size=40)]
        ]
        window = sg.Window("Cadastro de jogador").Layout(layout)
        button, values = window.Read()
        window.close()

        if button == '1':
            try:
                nome = values["nome"]
                data_nasc = values["data_nasc"]
                data_nasc = datetime(
                    year=int(data_nasc.split("/")[2]),
                    month=int(data_nasc.split("/")[1]),
                    day=int(data_nasc.split("/")[0])
                )
                window.close()
                return {
                    "nome": nome,
                    "data_nasc": data_nasc
                }
            except ValueError:
                self.escreve_mensagem("Data não existe!", "Data inválida")
            except IndexError:
                self.escreve_mensagem("A data deve ter o formato: dd/mm/yyyy", "Formato de data inválido")
            except Exception:
                self.escreve_mensagem("Algo inesperado ocorreu!")
            window.close()
            return

    def edita_jogador(self) -> dict:
        """
        Edita nome e data do jogador.
        """
        layout = [
            [sg.Text("Digite o nome do jogador a alterar:", size=40)],
            [sg.Input("", key="nome_antigo")],
            [sg.Text("Digite o novo nome:", size=40)],
            [sg.Input("", key="nome_novo")],
            [sg.Text("Digite a nova data de nascimento:", size=40)],
            [sg.Input("", key="data_nasc")],
            [sg.Button("Alterar", size=40, key="1")],
            [sg.Button("Cancelar", size=40, key="0")]
        ]
        window = sg.Window("Alterando um jogador").Layout(layout)
        button, values = window.Read()

        nome_antigo = values["nome_antigo"]
        nome_novo = values["nome_novo"]
        data_nasc = values["data_nasc"]
    
        if button == '1':
            try:
                data_nasc = data_nasc.split("/")
                data = datetime(
                    day=int(data_nasc[0]),
                    month=int(data_nasc[1]),
                    year=int(data_nasc[2])
                )
                window.close()
                return {
                    "nome_antigo": nome_antigo,
                    "nome_novo": nome_novo,
                    "data_nasc": data
                }
            except ValueError:
                self.escreve_mensagem("Data invalida! Digite apenas numeros!")
            except IndexError:
                self.escreve_mensagem("Data deve ser no formato dd/mm/yyyy")
        window.close()

    def remocao_jogador(self) -> dict:
        """
        Remove um jogador do jogo.
        """
        layout = [
            [sg.Text("Digite o nome do jogador a ser removido:")],
            [sg.Input("", key="nome")],
            [sg.Button("Remover", size=40, key="1")],
            [sg.Button("Cancelar", size=40, key="0")]
        ]
        window = sg.Window("Exclusão de jogador").Layout(layout)
        button, value = window.Read()
        if button == '1':
            window.close()
            return {
                "nome": value["nome"]
            }
        window.close()
        return None

    def mostra_jogadores(self, jogadores_dict) -> None:
        """
        Imprime os dados de um jogador.
        """
        contador = 1
        mensagem = ""
        for jogador in jogadores_dict:
            nome = jogador["nome"]
            score = jogador["score"]
            mensagem += f"{contador}: {nome} | Score: {score}\n\n"
            contador += 1
        layout = [
            [sg.Text(mensagem)],
            [sg.Button("Ok", key='0', size=40)]
        ]
        window = sg.Window("Lista jogadores").Layout(layout)
        button, _ = window.Read()
        if button == '0':
            window.close()
            return

    def escreve_mensagem(self, mensagem: str, titulo = "") -> None:
        """
        Imprime mensagem generica.
        """
        sg.Popup(titulo, mensagem)

    def confirma_jogador(self, jogador: Jogador) -> bool:
        """
        Pede confirmacao se o usuario quer selecionar tal jogador para o jogo.
        """
        layout = [
            [sg.Text(f"Tem certeza que deseja jogar com {jogador.nome}?")],
            [sg.Button("Sim", key='1')],
            [sg.Button("Não", key='0')]
        ]
        window = sg.Window("Confirmar jogador").Layout(layout)
        button, _ = window.Read()
        window.close()
        return button == '1'

    def carrega_jogador(self, jogadores) -> str:
        """
        Seleciona o numero de um jogador da lista de jogadores.
        @return -> int de 1 para cima.
        @return -> -1 se nao existirem jogadores cadastrados.
        @return -> None se o número inválido
        @return -> 0 se usuário voltou
        """
        contador = 1
        mensagem = ""
        for jogador in jogadores:
            mensagem += f"{contador}: {jogador}\n\n"
            contador += 1
        if contador > 1:
            layout = [
                [sg.Text(mensagem)],
                [sg.Text("Digite o nome do jogador:")],
                [sg.Input("", key="nome")],
                [sg.Button("Carregar", key='1', size=40)],
                [sg.Button("Retornar", key='0', size=40)]
            ]
            window = sg.Window("Carrega jogador").Layout(layout)
            button, values = window.Read()
            if button == '1':
                nome = values["nome"]
                window.close()
                return nome
            else:
                window.close()
                self.init_components()
                return 0
        else:
            return -1
