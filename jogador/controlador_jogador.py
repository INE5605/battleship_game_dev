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

    """
    Cadastra o usuario como jogador, com nome e data de nascimento
    """
    def cadastra_jogador(self) -> Jogador:
        dados_jogador = self.tela_jogador.adiciona_jogador()
        nome = dados_jogador["nome"]
        data_nasc = dados_jogador["data_nasc"]
        jogador = Jogador(nome=nome, data_nasc=data_nasc)
        self.jogadores.append(jogador)
        self.tela_jogador.escreve_mensagem("Jogador Cadastrado!")
        return jogador

    """
    @return jogador que tiver o nome
    """
    def __pega_jogador_por_nome(self, nome: str) -> Jogador:
        for jogador in self.jogadores:
            if jogador.nome == nome:
                return jogador
        return None

    """
    Remove o jogador pelo nome
    """
    def remove_jogador(self):
        dados_jogador = self.tela_jogador.remocao_jogador()
        nome = dados_jogador["nome"]
        jogador = self.__pega_jogador_por_nome(nome)
        self.jogadores.remove(jogador)
        self.tela_jogador.escreve_mensagem("Jogador removido!")

    """
    Lista todos os jogadores cadastrados
    """
    def lista_jogadores(self):
        self.tela_jogador.lista_jogadores(self.jogadores)

    """
    Altera o nome do jogador pelo nome
    """
    def altera_jogador(self):
        dados_jogador = self.tela_jogador.edita_nome()
        nome_antigo = dados_jogador["nome_antigo"]
        nome_novo = dados_jogador["nome_novo"]
        jogador = self.__pega_jogador_por_nome(nome_antigo)
        jogador.nome = nome_novo
        self.tela_jogador.escreve_mensagem("Jogador Alterado!")

    """
    Menu do controlador jogador
    """
    def abre_tela(self):
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

    """
    Retorna para a tela do controlador principal
    """
    def retorna(self):
        self.__controlador_principal.abre_tela()

    """
    Carrega o jogador pro jogo
    """
    def carrega_jogador(self) -> Jogador:
        numero_jogador = self.tela_jogador.carrega_jogador()
        return self.jogadores[numero_jogador - 1]
