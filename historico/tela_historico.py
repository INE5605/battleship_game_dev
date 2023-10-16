class TelaHistorico():
    def __init__(self):
        pass

    def pega_historico(self, historicos) -> int:
        print("\n*--------------------------------------*")
        print("*----------- Histórico do Jogador ---------*")
        print("*--------------------------------------*\n")
        print("Escolha a opcao")
        for index, historico in enumerate(historicos):
            print(len(historicos))
            print(f"{index} - {historico.data} - Vitória: {historico.vitoria}")

        opcoes_validas = list(range(len(historicos)))
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

    def exibe_movimentos(self, historico):
        movimentos = historico.movimentos
        for movimento in movimentos:
            print(f"Coordenada X: {movimento['coord_x']}   -   Coordenada Y: {movimento['coord_y']}   -   Acertou: {movimento['acertou']}    - Afundou: {movimento['afundou']}")
