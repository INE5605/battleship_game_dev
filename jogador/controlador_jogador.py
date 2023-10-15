from jogador.jogador import Jogador
from jogador.tela_jogador import TelaJogador


class CtrlJogador:
    def __init__(self, controlador_principal) -> None:
        self.tela_jogador = TelaJogador()
        self.controlador_principal = controlador_principal
        self.__jogadores = []

    @property
    def jogadores(self) -> list:
        return self.__jogadores

    @jogadores.setter
    def jogadores(self, jogadores) -> None:
        self.__jogadores = jogadores

    def cadastra_jogador(self) -> Jogador:
        """
        Cadastra o usuario como jogador, com nome e data de nascimento
        @return -> jogador: Jogador
        """
        dados_jogador = self.tela_jogador.adiciona_jogador()
        nome = dados_jogador["nome"]
        data_nasc = dados_jogador["data_nasc"]
        jogador = Jogador(nome=nome, data_nasc=data_nasc)
        self.jogadores.append(jogador)
        self.tela_jogador.escreve_mensagem("Jogador Cadastrado!")
        return jogador

    def __pega_jogador_por_nome(self, nome: str) -> Jogador:
        """
        @param1: nome do jogador (str)
        @return -> jogador que tiver o nome ou None caso nao exista.
        """
        for jogador in self.jogadores:
            if jogador.nome == nome:
                return jogador
        return None

    def remove_jogador(self):
        """
        Remove o jogador pelo nome
        """
        dados_jogador = self.tela_jogador.remocao_jogador()
        nome = dados_jogador["nome"]
        jogador = self.__pega_jogador_por_nome(nome)
        self.jogadores.remove(jogador)
        self.tela_jogador.escreve_mensagem("Jogador removido!")

    def lista_jogadores(self):
        """
        Lista todos os jogadores cadastrados.
        """
        self.tela_jogador.lista_jogadores(self.jogadores)

    def altera_jogador(self):
        """
        Altera o nome do jogador pelo nome.
        """
        dados_jogador = self.tela_jogador.edita_nome()
        nome_antigo = dados_jogador["nome_antigo"]
        nome_novo = dados_jogador["nome_novo"]
        jogador = self.__pega_jogador_por_nome(nome_antigo)
        jogador.nome = nome_novo
        self.tela_jogador.escreve_mensagem("Jogador Alterado!")

    def abre_tela(self):
        """
        Menu do controlador jogador.
        """
        menu = {
            1: self.cadastra_jogador,
            2: self.altera_jogador,
            3: self.lista_jogadores,
            4: self.remove_jogador,
            0: self.retorna
        }
        opcao = self.tela_jogador.tela_opcoes()
        menu[opcao]()
        self.tela_jogador.espera_interacao()
        self.abre_tela()

    def retorna(self):
        """
        Retorna para a tela do controlador principal.
        """
        self.controlador_principal.abre_tela()

    def carrega_jogador(self) -> Jogador: 
        """
        Seleciona o jogador pro jogo.
        """
        numero_jogador = self.tela_jogador.carrega_jogador(self.jogadores)
        if numero_jogador == -1:
            return self.jogadores[numero_jogador - 1]
        else:
            self.abre_tela()
