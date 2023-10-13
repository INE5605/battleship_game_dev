class Embarcacao:
	def __init__(self, tamanho: int):

		self.__tamanho = tamanho
		self.__shield = tamanho

	def afundou(self):
		'''Verifica se a embarcação foi afundada (todas as partes atingidas)'''

		return self.__shield == 0

	def recebe_ataque(self, coordenada) -> bool:
		'''Recebe um ataque em uma coordenada
		Atualiza self.shield e retorna True se afundou
		ou False se não afundou'''

		self.__shield -= 1

		print("Embarcação atacada. Registrar 1 ponto")

		if self.afundou():
			print("Embarcação afundou. Registrar 3 pontos")
		return self.afundou()
