class TelaPartida():
    def __init__(self):
        pass


    def tela_opcoes(self) -> int:
        print("\n*--------------------------------------*")
        print("*-----------Battleship War 1.0---------*")
        print("*--------------------------------------*\n")
        print("    Escolha a opcao")
        print("1 - Novo jogador")
        print("2 - Carregar jogador")
        print("3 - Histórico")
        print("0 - Voltar")

        opcoes_validas = [0, 1, 2]

        while True:
            try:
                opcao = int(input("Escolha a opcão: "))
                if opcao not in opcoes_validas:
                    raise ValueError(
                        "Opcao invalida, digite uma opcao valida."
                    )
                return opcao
            except ValueError:
                print("Digite apenas o numero da opcao escolhida.")

    def tela_opcoes_tela_partida(self) -> int:

        print("--- Tela ---")
        print("Escolha a opcao")
        print("1 - Bombardear inimigo")
        print("0 - Desistir da partida")

        opcoes_validas = [0, 1]

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if opcao not in opcoes_validas:
                    raise ValueError(
                        "Opcao invalida, digite uma opcao valida."
                    )
                return opcao
            except ValueError:
                print("Digite apenas o número da opção escolhida.")

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

    def tela_opcoes_escolhe_partida(self, opcoes_validas: str):

        print("--- Histórico de partidas ---")
        print("Escolha uma partida")

        opcoes_validas = range(int(opcoes_validas))

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

    def mostra_partidas(self, numero: str, nome_jogador: str,
                       data: str, terminou: str, desistiu: str,
                       vencedor: str) -> None:
        """
        Imprime dados de uma única partida
        """
        print(f"{numero}: Nome: {nome_jogador}  Data: {data}  Terminou: {terminou}")
        print(f"Desistiu: {desistiu}  Vencedor: {vencedor} \n")

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
