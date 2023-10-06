from datetime import datetime


class Jogador:
    def __init__(self, nome: str, data_nasc: datetime) -> None:
        self.__nome = nome
        self.__data_nasc = data_nasc
        self.__melhor_score = 0
        self.__score_acumulado = 0

    def __str__(self) -> str:
        to_str = f"Jogador: {self.nome}\n" + \
            "Melhor Score: {self.melhor_score}\n" + \
            f"Score Acumulado: {self.score_acumulado}\n"
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
    def melhor_score(self) -> int:
        return self.__melhor_score

    @melhor_score.setter
    def melhor_score(self, novo_melhor_score: int) -> None:
        self.__melhor_score = novo_melhor_score

    @property
    def score_acumulado(self) -> int:
        return self.__score_acumulado

    @score_acumulado.setter
    def score_acumulado(self, score_acumulado: int) -> None:
        self.__score_acumulado = score_acumulado

    def incrementa_score(self, score_inc) -> None:
        self.score_acumulado += score_inc
