from jogador.jogador import Jogador
from jogador.tela_jogador import TelaJogador


class CtrlJogador:
    def __init__(self, controlador_principal) -> None:
        self.__tela_jogador = TelaJogador()
        self.__controlador_principal = controlador_principal
        self.__jogadores = []

    @property
    def tela_jogador(self) -> TelaJogador:
        return self.__tela_jogador

    @property
    def jogadores(self) -> list:
        return self.__jogadores

    @jogadores.setter
    def jogadores(self, jogadores) -> None:
        self.__jogadores = jogadores

    def cadastra_jogador(self):
        dados_jogador = self.tela_jogador.adiciona_jogador()
        nome = dados_jogador["nome"]
        data_nasc = dados_jogador["data_nasc"]
        jogador = Jogador(nome=nome, data_nasc=data_nasc)
        self.jogadores.append(jogador)
        self.tela_jogador.escreve_mensagem("Jogador Cadastrado!")

    def __pega_jogador_por_nome(self, nome: str) -> Jogador:
        for jogador in self.jogadores:
            if jogador.nome == nome:
                return jogador
        return None

    def remove_jogador(self):
        dados_jogador = self.tela_jogador.remocao_jogador()
        nome = dados_jogador["nome"]
        jogador = self.__pega_jogador_por_nome(nome)
        self.jogadores.remove(jogador)
        self.tela_jogador.escreve_mensagem("Jogador removido!")

    def lista_jogadores(self):
        self.tela_jogador.lista_jogador(self.jogadores)

    def altera_jogador(self):
        dados_jogador = self.tela_jogador.edita_nome()
        nome_antigo = dados_jogador["nome_antigo"]
        nome_novo = dados_jogador["nome_novo"]
        jogador = self.__pega_jogador_por_nome(nome_antigo)
        jogador.nome = nome_novo
        self.tela_jogador.escreve_mensagem("Jogador Alterado!")

    def abre_tela(self, loop=True):
        menu = {
            1: self.cadastra_jogador,
            2: self.altera_jogador,
            3: self.lista_jogadores,
            4: self.remove_jogador,
            0: self.__controlador_principal.abre_tela
        }
        opcao = self.tela_jogador.tela_opcoes()
        menu[opcao]()
        self.tela_jogador.espera_interacao()
        if loop == True:
            self.abre_tela()

    def retorna(self):
        self.__controlador_principal.abre_tela()
