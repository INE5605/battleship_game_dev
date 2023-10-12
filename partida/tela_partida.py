class TelaPartida():
    def __init__(self):
        pass


    def tela_opcoes(self) -> int:
        print("--- Tela ---")
        print("Escolha a opcao")
        print("1 - Novo jogador")
        print("2 - Carregar jogador")
        print("0 - Voltar")

        opcoes_validas = [0, 1, 2]

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