from dao import DAO
from jogador.jogador import Jogador


class JogadorDao(DAO):
    def __init__(self, datasource='') -> None:
        super().__init__('jogador.pkl')

    def add(self, jogador: Jogador):
        if isinstance(jogador, Jogador):
            super().add(jogador.nome, jogador)

    def get(self, nome: str):
        return super().get(nome)

    def remove(self, nome: str):
        super().remove(nome)
