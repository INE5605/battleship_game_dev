class TelaEmbarcacao():
    def __init__(self):
        pass

    def tela_opcoes(self) -> int:
            print("--- Tela ---")
            print("Escolha a opcao")
            print("1 - Bote")
            print("2 - Submarino")
            print("3 - Fragata")
            print("4 - Porta aviões")
            print("0 - Retornar")

            opcoes_validas = [0, 1, 2, 3, 4]

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