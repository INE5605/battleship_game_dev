from dao import DAO
from partida.partida import Partida
from oceano.oceano import Oceano
from jogador.jogador import Jogador


class PartidaDAO(DAO):
    def __init__(self, datasource='') -> None:
        super().__init__('partida.pkl')

    def add(self, partida: Partida):
        if isinstance(partida, Partida):
            super().add(partida.id, partida)

    def get(self, id):
        return super().get(id)

    def remove(self, id: int):
        super().remove(id)
