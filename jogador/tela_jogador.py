from datetime import datetime
from jogador.jogador import Jogador
import PySimpleGUI as sg
from tela_abstrata import *


class TelaJogador(TelaAbstrata):
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

    def open(self):
        button, values = self.window.Read()
        return button, values

    def close(self):
        self.window.close()

    def tela_opcoes(self) -> int:
        button, _ = self.open()
        opcao = None
        if button == '0' or button == None:
            opcao = 0
        else:
            opcao = int(button)
        self.close()
        return opcao

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
        self.window = sg.Window("Cadastro de jogador").Layout(layout)
        button, values = self.open()

        if button == '1':
            try:
                data_nasc = values["data_nasc"]
                data_nasc = datetime(
                    year=int(data_nasc.split("/")[2]),
                    month=int(data_nasc.split("/")[1]),
                    day=int(data_nasc.split("/")[0])
                )
                self.close()
                return {
                    "nome": values["nome"],
                    "data_nasc": data_nasc
                }
            except ValueError:
                self.escreve_mensagem("Data invalida!\nFormato: dd/mm/yyyy")
            except IndexError:
                self.escreve_mensagem("A data deve ter o formato: dd/mm/yyyy")
            except Exception:
                self.escreve_mensagem("Algo inesperado ocorreu!")
            self.escreve_mensagem("Jogador cadastrado com sucesso!")
            self.close()
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
        self.window = sg.Window("Alterando um jogador").Layout(layout)
        button, values = self.open()

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
                return {
                    "nome_antigo": nome_antigo,
                    "nome_novo": nome_novo,
                    "data_nasc": data
                }
            except ValueError:
                self.escreve_mensagem("Data invalida! Digite apenas numeros!")
            except IndexError:
                self.escreve_mensagem("Data deve ser no formato dd/mm/yyyy")
            self.close()

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
        self.window = sg.Window("Exclusão de jogador").Layout(layout)
        button, value = self.open()
        if button == '1':
            return {
                "nome": value["nome"]
            }
        else:
            self.escreve_mensagem("Jogador não encontrado!")
            self.close()
            return

    def mostra_jogador(self, jogador_dict) -> None:
        """
        Imprime os dados de um jogador.
        """
        jogador: Jogador = jogador_dict["jogador"]
        sg.Popup(f"Jogador: {jogador.nome}\n Score: {jogador.score}")

    def escreve_mensagem(self, mensagem: str) -> None:
        """
        Imprime mensagem generica.
        """
        sg.Popup(mensagem)

    def confirma_jogador(self, jogador: Jogador) -> bool:
        """
        Pede confirmacao se o usuario quer selecionar tal jogador para o jogo.
        """
        layout = [
            [sg.Text(f"Tem certeza que deseja jogar com {jogador.nome}?")],
            [sg.Button("Sim", key='1')],
            [sg.Button("Não", key='0')]
        ]
        self.window = sg.Window("Confirmar jogador").Layout(layout)
        button, _ = self.open()
        return button == '1'

    def carrega_jogador(self, jogadores) -> int:
        """
        Seleciona o numero de um jogador da lista de jogadores.
        @return -> int de 1 para cima.
        @return -> -1 se nao existirem jogadores cadastrados.
        """
        contador = 1
        mensagem = ""
        for jogador in jogadores:
            mensagem += f"{contador}: {jogador}\n\n"
            contador += 1
        if contador > 1:
            while True:
                layout = [
                    [sg.Text(mensagem)],
                    [sg.Text("Digite o numero do jogador:")],
                    [sg.Input("", key="numero")],
                    [sg.Button("Carregar", key='1', size='40')],
                    [sg.Button("Retornar", key='0', size='40')]
                ]
                self.window = sg.Window("Exclusão de jogador").Layout(layout)
                button, values = self.open()
                if button == '1':
                    try:
                        numero = int(values["numero"])
                        if numero > contador or numero < 1:
                            raise ValueError
                    except:
                        self.escreve_mensagem("Numero invalido")
                    else:
                        return numero
                else:
                    self.init_components()
                self.escreve_mensagem("Nao ha jogadores cadastrados no momento.")
                return -1
