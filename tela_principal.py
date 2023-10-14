class TelaPrincipal():
    def __init__(self):
        pass


    def tela_opcoes(self) -> int:
        print("\n*--------------------------------------*")
        print("*-----------Battleship War 1.0---------*")
        print("*--------------------------------------*\n")
        print("    Escolha a opcao")
        print("1 - Jogador")
        print("2 - Iniciar Jogo")
        print("3 - Develop: Abrir controlador principal")
        print("4 - Develop: Abrir novo Jogador")
        print("5 - Develop: Abrir Jogador existente")
        print("0 - Sair")

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