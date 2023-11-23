from abc import ABC, abstractmethod

class Embarcacao(ABC):
	def __init__(self, id: int, tamanho: int, letra: str):

		self.__id = id
		self.__tamanho = tamanho
		self.__shield = tamanho
		self.__letra = letra
		self.__posicoes = list()
		self.__horizontal = True
		self.__sprites = []

	@property
	def id(self):
		return self.__id

	@property
	def tamanho(self):
		return self.__tamanho
	
	@property
	def shield(self):
		return self.__shield
	
	@property
	def letra(self):
		return self.__letra

	@property
	def posicoes(self):
		return self.__posicoes

	@property
	def horizontal(self):
		return self.__horizontal

	@horizontal.setter
	def horizontal(self, horizontal: bool):
		self.__horizontal = horizontal

	@property
	def sprites(self):
		return self.__sprites

	def afundou(self):
		'''Verifica se a embarcação foi afundada (todas as partes atingidas)'''

		return self.__shield == 0

	def recebe_ataque(self) -> bool:
		'''Recebe um ataque em uma coordenada
		Atualiza self.shield e retorna True se afundou
		ou False se não afundou'''

		self.__shield -= 1
		
		return True, self.afundou()
	
	def adiciona_posicoes(self, posicoes: list):
		self.__posicoes.append(posicoes)

	@abstractmethod
	def possiveis_sprites(self, horizontal):
		pass
	
	def adiciona_sprites(self, horizontal):
		sprites = self.possiveis_sprites(horizontal)
		for sprite in sprites:
			self.__sprites.append(sprite)
