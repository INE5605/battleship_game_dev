from embarcacao.embarcacao import Embarcacao
from embarcacao.tipos.bote import Bote
from oceano.oceano import Oceano
from oceano.tela_oceano import TelaOceano
from oceano.excecoes.oceano_pequeno_exception import OceanoPequenoException
from oceano.excecoes.embarcacao_fora_oceano_exception import EmbarcacaoForaOceanoException
from oceano.excecoes.posicao_nao_vazia_exception import PosicaoNaoVaziaException
from random import randint
from datetime import datetime as Datetime
import PySimpleGUI as sg


class CtrlOceano:
    def __init__(self, controlador_principal) -> None:
        self.controlador_principal = controlador_principal
        self.tela_oceano = TelaOceano()
        self.__oceano_jogador: Oceano = None
        self.__oceano_computador: Oceano = None

    @property
    def oceano_jogador(self) -> Oceano:
        return self.__oceano_jogador

    @property
    def oceano_computador(self) -> Oceano:
        return self.__oceano_computador

    def cadastra_oceano(self):
        """ Cadastra oceano do jogador ou computador
            @return -> oceano_jogador: Oceano, oceano_computador: Oceano
        """
        dados_oceanos = self.tela_oceano.cadastra_oceano()
        try:
            dimensao_x = int(dados_oceanos["dimensao_x"])
            dimensao_y = int(dados_oceanos["dimensao_y"])
            if dimensao_x < 5 or dimensao_y < 5:
                raise OceanoPequenoException()
        except ValueError:
            self.tela_oceano.imprime_mensagem(
                "As dimensoes do oceano devem ser numeros inteiros!"
            )
        except OceanoPequenoException as error:
            self.tela_oceano.imprime_mensagem(error)
            
        self.__oceano_jogador = Oceano(dimensao_x, dimensao_y, 1)
        self.__oceano_computador = Oceano(dimensao_x, dimensao_y, 2)

        self.oceano_jogador.escondido = self.cria_oceano_escondido()
        self.oceano_jogador.layout = self.cria_oceano_layout(1)

        self.oceano_computador.escondido = self.cria_oceano_escondido()
        self.oceano_computador.layout = self.cria_oceano_layout(2)
        self.oceano_computador.escondido_layout = self.cria_oceano_layout(2)

        self.__preencher_oceano_com_embarcacoes(metodo = self.__add_embarcacao_random)
        self.__preencher_oceano_com_embarcacoes(metodo = self.__add_embarcacao_set)

        self.oceano_jogador.escondido_layout = self.oceano_jogador.layout

        return self.oceano_jogador, self.oceano_computador

    def pergunta_sera_horizontal(self) -> bool:
        """
        Define a direcao da embarcacao do jogador.
        @Return -> True se horizontal, False se vertical.
        """
        while True:
            try:
                horizontal = self.tela_oceano.pega_direcao_embarcacao_horizontal()
            except ValueError:
                self.tela_oceano.imprime_mensagem("A sua resposta deve ser 'S' OU 'N'!")
            else:
                return horizontal

    def preencher_oceano_jogador(
        self,
        embarcacoes: list
    ):
        """
        Preenche posicoes do oceano do usuario com embarcacoes.
        """
        for embarcacao in embarcacoes:
            while True:
                try:
                    dados_posicao = self.tela_oceano.pega_posicao_para_preencher_embarcacao()
                    is_horizontal = dados_posicao['horizontal']
                    posicoes = self.__gera_posicoes_embarcacoes_set(
                        embarcacao,
                        dados_posicao,
                        is_horizontal
                    )
                    adicionou = self.__adiciona_embarcacao(
                        posicoes,
                        is_horizontal,
                        self.oceano_jogador,
                        embarcacao
                    )
                    if adicionou:
                        break
                except ValueError:
                    self.tela_oceano.imprime_mensagem(
                        "Os dados de posicao nao sao numeros inteiros!"
                    )
                except IndexError:
                    self.tela_oceano.imprime_mensagem(
                        "A posicao final indicada eh maior do que a posicao do oceano"
                    )
                except EmbarcacaoForaOceanoException as erro:
                    self.tela_oceano.imprime_mensagem(erro)

    def __preencher_oceano_com_embarcacoes(self, metodo):
        """
        Preenche o Oceano do computador com as 8 embarcacoes.
        """

        quantidades = {
            "porta_avioes": 1,
            "fragata": 2,
            "submarino": 2,
            "bote": 3
        }
        for tipo, quantidade in quantidades.items():
            for _ in range(quantidade):
                embarcacao = self.controlador_principal.controlador_embarcacao.criar_embarcacoes(tipo)
                metodo(embarcacao)

    def __add_embarcacao_random(
        self,
        embarcacao: Embarcacao,
    ):
        """
        Adiciona uma embarcacao aleatoriamente no oceano do computador.
        """

        contador = 0
        while True:
            is_horizontal = self.__sera_horizontal_random()
            posicoes = self.__gera_posicoes_embarcacao_random(
                embarcacao, is_horizontal
            )

            adicionou = self.__adiciona_embarcacao(
                posicoes,
                is_horizontal,
                self.__oceano_computador,
                embarcacao
            )

            if adicionou:
                break

            contador += 1
            if contador > 150:
                self.tela_oceano.imprime_mensagem(
                    "Não houve espaço suficiente para cadastrar todas as embarcações!"
                )
                return self.controlador_principal.abre_tela()

    def __add_embarcacao_set(
        self,
        embarcacao: Embarcacao
    ):
        """
        Adiciona uma embarcacao com posição definida pelo usuário no oceano.
        """
        while True:
            try:
                dados_posicao = self.tela_oceano.pega_posicao_para_preencher_embarcacao(
                    self.oceano_jogador,
                    embarcacao
                )
                is_horizontal = dados_posicao['horizontal']
                posicoes = self.__gera_posicoes_embarcacoes_set(
                    embarcacao,
                    dados_posicao,
                    is_horizontal
                )
                if self.__adiciona_embarcacao(
                    posicoes,
                    is_horizontal,
                    self.__oceano_jogador,
                    embarcacao
                ):
                    for coord_x, coord_y in posicoes:
                        self.edita_oceano_escondido(oceano=self.__oceano_jogador,
                        coord_x = coord_x,
                        coord_y = coord_y,
                        value = embarcacao.letra)
                    break
            except EmbarcacaoForaOceanoException as e:
                self.tela_oceano.imprime_mensagem(e)
            self.tela_oceano.imprime_mensagem(
                "Embarcação não pode ser adicionada nessa posição. Por favor tente outra posição"
            )

    def __sera_horizontal_random(self):
        is_horizontal = (True, False)[randint(0, 1) == 0]
        return is_horizontal

    def __adiciona_embarcacao(
        self,
        posicoes: list,
        horizontal: bool,
        oceano: Oceano,
        embarcacao: Embarcacao
    ):
        """
        Se as posicoes estiverem desocupadas preenche com a embarcacao
        @return -> true se adicionou, false se posições já estavam ocupadas
        """

        try:
            for posicao in posicoes:
                if (oceano.verifica_posicao_nao_vazia(posicao[0], posicao[1]) or 
                    oceano.verifica_posicao_negativa(posicao[0], posicao[1]) or
                    oceano.verifica_posicao_fora_matriz(posicao[0], posicao[1])):
                    break
            else:
                oceano.posicionar_embarcacao(posicoes, embarcacao)
                self.controlador_principal.controlador_embarcacao.edita_posicoes_e_sprites(embarcacao, posicoes, horizontal)
                for i in range(len(posicoes)):
                    oceano.edita_oceano_layout(posicoes[i][0], posicoes[i][1], embarcacao.sprites[i])
                return True

        except PosicaoNaoVaziaException as e:
            self.tela_oceano.imprime_mensagem(e)
        return False

    def __gera_posicoes_embarcacao_random(
        self,
        embarcacao: Embarcacao,
        is_horizontal: bool
    ) -> list:
        posicoes = []
        posicao_y = randint(
            0, self.__oceano_computador.dimensao_y - 1
        )
        posicao_x = randint(
            0, self.__oceano_computador.dimensao_x - 1
        )
        posicoes.append([posicao_x, posicao_y])

        if is_horizontal:
            for i in range(1, embarcacao.tamanho):
                posicoes.append(
                    [posicao_x + i, posicao_y]
                )
        else:
            for i in range(1, embarcacao.tamanho):
                posicoes.append(
                    [posicao_x, posicao_y + i]
                )
        return posicoes

    def __gera_posicoes_embarcacoes_set(
        self,
        embarcacao: Embarcacao,
        dados_posicao: dict,
        is_horizontal: bool = True
    ) -> list:
        """
        Gera as posicoes da embarcacao com base no tamanho da embarcacao
        Definido pela posicao final que o usuario escolheu
        @return -> lista de inteiros com as posicoes no formato:
        [posicao_x, posicao_y]
        """
        posicao_x0 = int(dados_posicao["posicao_x"])
        posicao_y0 = int(dados_posicao["posicao_y"])
        posicoes = [[posicao_x0, posicao_y0]]
        
        if isinstance(embarcacao, Bote):
            return posicoes

        else:
            for i in range(1, embarcacao.tamanho):
                if is_horizontal:
                    posicao_x = posicao_x0 + i
                    posicoes.append([posicao_x, posicao_y0])
                else:
                    posicao_y = posicao_y0 + i
                    posicoes.append([posicao_x0, posicao_y])
            for posicao in posicoes:
                if posicao[0] > self.oceano_jogador.dimensao_x or \
                posicao[1] > self.oceano_jogador.dimensao_y:
                    raise EmbarcacaoForaOceanoException
            return posicoes

    def cria_oceano_escondido(self):
        '''Cria oceano que irá ser referência para o jogador, que irá apenas mostrar necessárias ao jogador.'''

        oceano_escondido = [ ["~"]*self.oceano_jogador.dimensao_x for _ in range(self.oceano_jogador.dimensao_y)]
        return oceano_escondido
    
    def cria_oceano_layout(self, player):
        '''Cria layout do oceano que irá ser referência para o jogador, que irá apenas mostrar necessárias ao jogador.'''

        oceano_layout = [
        [sg.Button(" ", key = f"Frame{player} {j} {i}",
                   button_color=('LightBlue4'), image_filename ='./imagens/oceano.png', image_size=(50, 50),
                   image_subsample=1, border_width=0, pad=(1, 1)) for j in range(self.oceano_jogador.dimensao_y)] for i in range(self.oceano_jogador.dimensao_x)
    ]
        return oceano_layout
        
    def edita_oceano_escondido(self, oceano:Oceano, coord_x:int, coord_y:int, value:str):
        '''Edita oceano escondido, atribuindo um valor value a dadas coordenadas'''

        oceano.edita_oceano_escondido(coord_x, coord_y, value)

    def edita_oceano_layout(self, oceano:Oceano, coord_x:int, coord_y:int, value:str):
        '''Edita oceano definido em forma de um layout do PySimpleGui
        ao receber coordenada e o novo valor de tal coordenada
        value deve ser um png por exemplo "./oceano"'''

        oceano.edita_oceano_layout(coord_x, coord_y, value)

    def edita_oceano_escondido_layout(self, oceano:Oceano, coord_x:int, coord_y:int, value:str):
        '''Edita oceano definido em forma de um layout do PySimpleGui
        ao receber coordenada e o novo valor de tal coordenada
        value deve ser um png por exemplo "./oceano"'''

        oceano.edita_oceano_escondido_layout(coord_x, coord_y, value)

    def bombardeia_oceano(self, bombardeia_quem: str, oceano_jogador: Oceano, oceano_computador: Oceano):
        '''
        Bombardeia jogador ou computador, definido
        por bombardeia_quem e oceano.\n
        Edita o oceano de acordo com o seu valor no campo (colocando x ou o).
        Caso acerte, jogador/computador joga denovo.
        No final, os pontos recebidos são retornados.
        '''

        pontos_ganhos = 0
        jogadas = []

        while True:
            jogada = {
                "acertou": False,
                "afundou": False
            }
            vencedor = None

            if bombardeia_quem == 'computador':
                while True:
                    oceano = oceano_computador
                    event, _ = self.tela_oceano.tela_bombardeia(oceano_jogador, oceano_computador)

                    if event == "desistir":
                        self.controlador_principal.controlador_partida.desiste_pergunta()

                    if event != None:
                        # Dev: corrigir esse contorno.
                        #As vezes clicando em algo aparece o retorno tipo 511 ao invés de 5
                        _, coord_x, coord_y = event.split()
                        coord_x, coord_y = int(coord_x), int(coord_y)
                        break

            if bombardeia_quem == 'jogador':
                oceano = oceano_jogador
                coord_x, coord_y = self.__bombardeia_jogador(oceano)

            valor = oceano.campo[coord_y][coord_x]
            jogada["coord_x"] = coord_x
            jogada["coord_y"] = coord_y

            if valor == ' ':
                self.edita_oceano_escondido(oceano, coord_x, coord_y, 'o')
                self.edita_oceano_escondido_layout(oceano, coord_x, coord_y, './imagens/nada')
                jogadas.append(jogada)
                break
            else:
                self.edita_oceano_escondido(oceano, coord_x, coord_y, 'x')
                self.edita_oceano_escondido_layout(oceano, coord_x, coord_y, './imagens/explosao')
                acertou, afundou = valor.recebe_ataque()
                jogada["acertou"] = acertou
                jogada["afundou"] = afundou
                jogada["data"] = Datetime.now().strftime("%d/%m/%Y")
                jogadas.append(jogada)
                
                if acertou:
                    if bombardeia_quem == 'computador':
                        self.tela_oceano.escreve_mensagem("Embarcação atacada: 1 ponto")
                    pontos_ganhos += 1
                if afundou:
                    if bombardeia_quem == 'computador':
                        self.tela_oceano.escreve_mensagem("Embarcação afundada: 3 pontos")
                    pontos_ganhos += 3
                    vencedor = self.verifica_vencedor(bombardeia_quem, oceano)
                    for i in range(len(oceano.campo[coord_y][coord_x].posicoes[0])):
                        posicao = oceano.campo[coord_y][coord_x].posicoes[0][i]
                        sprite = oceano.campo[coord_y][coord_x].sprites[i]
                        self.oceano_computador.edita_oceano_escondido_layout_afundado(posicao[0],
                                                                         posicao[1],
                                                                         sprite)

            if vencedor != None:
                controlador_partida = self.controlador_principal.controlador_partida
                partida = self.controlador_principal.controlador_partida.partida_atual()
                partida.vencedor = (partida.jogador, "Computador")[vencedor == "jogador"]
                partida.terminou = True
                if vencedor == "jogador":
                    partida.vencedor = partida.jogador
                    self.tela_oceano.escreve_mensagem(f"Parabéns jogador {partida.vencedor}! Você venceu!")
                else:
                    partida.vencedor = vencedor
                    self.tela_oceano.escreve_mensagem(f"Fim do jogo! Vencedor: {vencedor}")
                self.controlador_principal.abre_tela()

        return {
            "pontos_ganhos": pontos_ganhos,
            "jogadas": jogadas
        }

    def verifica_vencedor(
        self,
        bombardeia_quem: str,
        oceano: Oceano
    ):
        campo = oceano.campo
        for linha in campo:
            for posicao in linha:
                if isinstance(posicao, Embarcacao):
                    if posicao.shield > 0:
                        return None
        return ("computador", "jogador")[bombardeia_quem == "computador"]

    def __bombardeia_jogador(self, oceano: Oceano):
        coord_x = randint(0, oceano.dimensao_x - 1)
        coord_y = randint(0, oceano.dimensao_y - 1)
        return coord_x, coord_y

    def __show_layout(self, layout):
        window = sg.Window('Layout Viewer', layout, element_justification='c')
        
        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED:
                break

        window.close()