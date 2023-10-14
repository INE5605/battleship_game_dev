from datetime import datetime
from jogador.jogador import Jogador


class TelaJogador:
    def tela_opcoes(self) -> int:
        print("--- Tela Jogador ---")
        print("Escolha a opcao")
        print("1 - Adicionar jogador")
        print("2 - Alterar jogador")
        print("3 - Listar jogadores")
        print("4 - Excluir jogador")
        print("5 - Jogar com Jogador ja cadastrado")
        print("0 - Retornar")

        opcoes_validas = [0, 1, 2, 3, 4, 5]

        while True:
            try:
                opcao = int(input("Escolha a opcao: "))
                if opcao not in opcoes_validas:
                    raise ValueError(
                        "Opcao invalida, digite uma opcao valida."
                    )
                return opcao
            except ValueError:
                print("Digite apenas o numero da opcao escolhida.")

    def adiciona_jogador(self) -> dict:
        nome = input("Digite o seu nome: ")
        while True:
            data_nasc = input("Digite a sua data de nascimento (dd/mm/yyyy): ")
            try:
                data_nasc = datetime(
                    year=int(data_nasc.split("/")[2]),
                    month=int(data_nasc.split("/")[1]),
                    day=int(data_nasc.split("/")[0])
                )
                return {
                    "nome": nome,
                    "data_nasc": data_nasc
                }
            except ValueError:
                print("Data invalida")

    def edita_nome(self) -> dict:
        nome_antigo = input("Digite o nome do jogador: ")
        nome_novo = input("Digite o novo nome do jogador: ")
        return {
            "nome_antigo": nome_antigo,
            "nome_novo": nome_novo
        }

    def remocao_jogador(self) -> dict:
        nome = input("Digite o nome do jogador a ser removido: ")
        return {
            "nome": nome
        }

    def lista_jogadores(self, jogadores) -> None:
        print("Jogadores Cadastrados no Sistema:\n")
        for jogador in jogadores:
            print(jogador)

    def escreve_mensagem(self, mensagem: str) -> None:
        print(mensagem)

    def espera_interacao(self) -> None:
        input("Aperte Enter para continuar!")

    def novo_jogador(self) -> str:
        nome = input("Digite o nome do jogador: ")
        return nome

    def confirma_jogador(self, jogador: Jogador) -> bool:
        resposta = input(
            f"Tem certeza que deseja jogar com {jogador}(S / N)?"
        ).upper()
        return resposta == 'S'

    def carrega_jogador(self, jogadores) -> int:
        contador = 1
        for jogador in jogadores:
            print(f"{contador}: {jogador}")
            contador += 1
        while True:
            try:
                numero = int(input("Digite o numero do jogador:"))
                if numero > contador or numero < 1:
                    raise ValueError
            except:
                print("Numero invalido")
            else:    
                return numero
