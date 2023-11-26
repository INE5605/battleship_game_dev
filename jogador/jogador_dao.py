from dao import DAO
from jogador.jogador import Jogador


class JogadorDAO(DAO):
    def __init__(self, datasource='') -> None:
        super().__init__('jogador.pkl')
        self.get_all()

    def add(self, jogador: Jogador):
        if isinstance(jogador, Jogador):
            super().add(jogador.nome, jogador)

    def get(self, nome: str):
        return super().get(nome)

    def remove(self, nome: str):
        super().remove(nome)

    def update(self, nome_antigo: str, nome_atual: str, jogador: Jogador):
        super().remove(nome_antigo)
        super().add(nome_atual, jogador)

    def get_all(self):
        return super().get_all()
