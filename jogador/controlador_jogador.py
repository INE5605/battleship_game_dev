from jogador.jogador_jah_existe_exception import JogadorJahExisteException
from jogador.tela_jogador import TelaJogador
from jogador.jogador_dao import JogadorDAO
from jogador.jogador import Jogador
from jogador.nome_vazio_exception import NomeVazioException
from controlador import Controlador
from operator import attrgetter
from objeto_nao_existe_exception import ObjetoNaoExisteException


class CtrlJogador(Controlador):
    def __init__(self, controlador_principal) -> None:
        super().__init__()
        self.tela_jogador = TelaJogador()
        self.controlador_principal = controlador_principal
        self.__jogador_dao = JogadorDAO()

    @property
    def jogadores(self) -> dict[JogadorDAO]:
        return self.__jogador_dao.get_all()

    def cadastra_jogador(self) -> Jogador:
        """
        Cadastra o usuario como jogador, com nome e data de nascimento
        @return -> jogador: Jogador
        """
        while self.mantem_tela_aberta:
            dados_jogador = self.tela_jogador.adiciona_jogador()
            if dados_jogador == None:
                return
            nome = dados_jogador["nome"]
            data_nasc = dados_jogador["data_nasc"]
            try:
                if nome == "":
                    raise NomeVazioException
                if self.__jogador_dao.get(nome) is not None:
                    raise JogadorJahExisteException()
                jogador = Jogador(nome=nome, data_nasc=data_nasc)
                self.__jogador_dao.add(jogador)
                self.tela_jogador.escreve_mensagem("Jogador Cadastrado!")
                return jogador
            except NomeVazioException as e:
                self.tela_jogador.escreve_mensagem("O jogador precisa possuir um nome válido", e)
            except JogadorJahExisteException as e:
                self.tela_jogador.escreve_mensagem(e, "Erro")

    def __pega_jogador_por_nome(self, nome: str) -> Jogador:
        """
        @param1: nome do jogador (str)
        @return -> jogador que tiver o nome ou None caso nao exista.
        """
        jogador = self.__jogador_dao.get(nome)
        return jogador

    def remove_jogador(self):
        """
        Remove o jogador pelo nome
        """
        dados_jogador = self.tela_jogador.remocao_jogador()
        if dados_jogador == None:
            return
        nome = dados_jogador["nome"]
        try:
            if nome == "":
                raise NomeVazioException
            self.__jogador_dao.remove(nome)
        except ObjetoNaoExisteException as e:
            self.tela_jogador.escreve_mensagem("Jogador nao encontrado!", e)
        except NomeVazioException as e:
            self.tela_jogador.escreve_mensagem("Preencha o nome do jogador a ser removido!", e)
        else:
            self.tela_jogador.escreve_mensagem("Jogador removido!")

    def lista_jogadores(self):
        """
        Lista todos os jogadores cadastrados.
        """
        if len(self.jogadores) == 0:
            self.tela_jogador.escreve_mensagem(
                "Nao ha jogadores cadastrados no sistema!", "Lista de jogadores"
            )
        else:
            jogadores = []
            for jogador in self.jogadores:
                jogador_dicionario = {
                    "nome": jogador.nome,
                    "score": jogador.score
                }
                jogadores.append(jogador_dicionario)
                self.tela_jogador.mostra_jogadores(jogadores)

    def altera_jogador(self):
        """
        Altera o nome e a data de nascimento do jogador pelo nome.
        """
        dados_jogador = self.tela_jogador.edita_jogador()
        if dados_jogador == "" or dados_jogador == None:
            return
        nome_antigo = dados_jogador["nome_antigo"]
        nome_novo = dados_jogador["nome_novo"]
        data_nasc = dados_jogador["data_nasc"]
        if nome_antigo == "" or nome_novo == "":
            self.tela_jogador.escreve_mensagem("Preencha todos os campos!", "Campo vazio")
            return
        jogador = self.__pega_jogador_por_nome(nome_antigo)
        if isinstance(jogador, Jogador):
            jogador.nome = nome_novo
            jogador.data_nasc = data_nasc
            self.__jogador_dao.update(nome_antigo, jogador.nome, jogador)
            self.tela_jogador.escreve_mensagem("Jogador Alterado!")
            self.lista_jogadores()
        else:
            self.tela_jogador.escreve_mensagem("Jogador nao encontrado!")
            self.lista_jogadores()

    def abre_tela(self):
        """
        Menu do controlador jogador.
        """
        menu = {
            1: self.cadastra_jogador,
            2: self.altera_jogador,
            3: self.lista_jogadores,
            4: self.remove_jogador,
            5: self.carrega_jogador,
            0: self.retorna
        }
        opcao = self.tela_jogador.tela_opcoes()
        menu[opcao]()
        self.abre_tela()

    def retorna(self):
        """
        Retorna para a tela do controlador principal.
        """
        self.controlador_principal.abre_tela()

    def carrega_jogador(self): 
        """
        Seleciona o jogador pro jogo.
        """
        nome_jogador = self.tela_jogador.carrega_jogador(self.jogadores)
        try:
            if nome_jogador == "":
                raise NomeVazioException
        except NomeVazioException:
            self.tela_jogador.escreve_mensagem("O nome deve ser preenchido!")
        jogador = self.__jogador_dao.get(nome_jogador)
        if (isinstance(jogador, Jogador)):
            self.controlador_principal.controlador_partida.carrega_jogador_inicia_jogo(jogador)
        else:
            self.tela_jogador.escreve_mensagem("Não há jogador com determinado nome!", "Jogador não existe")
            self.abre_tela()

    def lista_jogador_por_score(self) -> Jogador:
        jogadores_ordenados = sorted(self.__jogadores, key=attrgetter('score'), reverse=True)
        numero_jogador = self.tela_jogador.carrega_jogador(jogadores_ordenados)
        if numero_jogador >= 1:
            return jogadores_ordenados[numero_jogador - 1]
        else:
            self.tela_jogador.escreve_mensagem("Jogador nao existente!")
            self.abre_tela()
