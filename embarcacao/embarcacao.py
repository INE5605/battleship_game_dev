class Embarcacao:
	def __init__(self, tamanho: int, letra: str):

		self.__tamanho = tamanho
		self.__shield = tamanho
		self.__letra = letra

	@property
	def tamanho(self):
		return self.__tamanho
	
	@property
	def shield(self):
		return self.__shield
	
	@property
	def letra(self):
		return self.__letra

	def afundou(self):
		'''Verifica se a embarcação foi afundada (todas as partes atingidas)'''

		return self.__shield == 0

	def recebe_ataque(self) -> bool:
		'''Recebe um ataque em uma coordenada
		Atualiza self.shield e retorna True se afundou
		ou False se não afundou'''

		self.__shield -= 1
		
		return True, self.afundou()

