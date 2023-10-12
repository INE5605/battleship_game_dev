class Embarcacao:
	def __init__(self, tamanho):

		self.__tamanho = tamanho
		self.__atingido = [False]*tamanho

		def afundou(self):
			# Verifica se a embarcação foi afundada (todas as partes atingidas)

			return all(self.__atingido)

		def recebe_ataque(self, coordenada):
			# Recebe um ataque em uma coordenada
			# Atualiza self.atingido para marcar a parte da embarcação atingida

			self.__atingido[coordenada] = True
			return None
