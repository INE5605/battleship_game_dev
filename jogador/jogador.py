from datetime import datetime


class Jogador:
    def __init__(self, nome: str, data_nasc: datetime) -> None:
        self.__nome = nome
        self.__data_nasc = data_nasc
        self.__score = 0

    def __str__(self) -> str:
        """
        Imprime o nome e o score acumulado do jogador.
        """
        to_str = f"Jogador: {self.nome} | Score Acumulado: {self.score}"
        return to_str

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def data_nasc(self) -> datetime:
        return self.__data_nasc

    @data_nasc.setter
    def data_nasc(self, data_nasc: datetime) -> None:
        self.__data_nasc = data_nasc

    @property
    def score(self) -> int:
        return self.__score

    @score.setter
    def score(self, score_acumulado: int) -> None:
        self.__score = score_acumulado

    def incrementa_score(self, score_inc) -> None:
        """
        Aumenta o score do jogador.
        @param1: score a ser incrementado
        """
        self.score += score_inc
