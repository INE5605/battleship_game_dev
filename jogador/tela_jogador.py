from datetime import datetime
from jogador.jogador import Jogador


class TelaJogador:
    def tela_opcoes(self) -> int:
        """
        Menu de tela jogador.
        """
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
        """
        Adiciona um jogador ao jogo.
        Pede nome e data de nascimento.
        """
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
                print("Data invalida!\nFormato: dd/mm/yyyy")
            except IndexError:
                print("A data deve ter o formato: dd/mm/yyyy")
            except Exception:
                print("Algo inesperado ocorreu!")

    def edita_jogador(self) -> dict:
        """
        Edita nome e data do jogador.
        """
        nome_antigo = input("Digite o nome do jogador: ")
        nome_novo = input("Digite o novo nome do jogador: ")
        while True:
            try:
                data_nasc = input("Digite a nova data de nascimento: ").split("/")
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
                print("Data invalida! Digite apenas numeros!")
            except IndexError:
                print("Data deve ser no formato dd/mm/yyyy")

    def remocao_jogador(self) -> dict:
        """
        Remove um jogador do jogo.
        """
        nome = input("Digite o nome do jogador a ser removido: ")
        return {
            "nome": nome
        }

    def mostra_jogador(self, jogador_dict) -> None:
        """
        Imprime os dados de um jogador.
        """
        print(jogador_dict["jogador"])

    def escreve_mensagem(self, mensagem: str) -> None:
        """
        Imprime mensagem generica.
        """
        print(mensagem)

    def espera_interacao(self) -> None:
        """
        Espera o usuario interagir.
        """
        input("Aperte Enter para continuar!")

    def confirma_jogador(self, jogador: Jogador) -> bool:
        """
        Pede confirmacao se o usuario quer selecionar tal jogador para o jogo.
        """
        resposta = input(
            f"Tem certeza que deseja jogar com {jogador}(S / N)?"
        ).upper()
        return resposta == 'S'

    def carrega_jogador(self, jogadores) -> int:
        """
        Seleciona o numero de um jogador da lista de jogadores.
        @return -> int de 1 para cima.
        @return -> -1 se nao existirem jogadores cadastrados.
        """
        contador = 1
        for jogador in jogadores:
            print(f"{contador}: {jogador}")
            contador += 1
        if contador > 1:
            while True:
                try:
                    numero = int(input("Digite o numero do jogador:"))
                    if numero > contador or numero < 1:
                        raise ValueError
                except:
                    print("Numero invalido")
                else:
                    return numero
        else:
            print("Nao ha jogadores cadastrados no momento.")
            return -1
