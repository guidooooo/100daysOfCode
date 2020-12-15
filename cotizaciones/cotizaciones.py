
import json


class cotizacion():

	def __init__(self, source):

		if source.lower() == 'ripio': 
			self.__source =  Ripio()
		elif source.lower() == 'dolarSi': 
			self.__source = DolarSi()
		elif source.lower() == 'coinmarketcap': 
			self.__source = CoinMarketCap()
		else:
			error_message = "Source invalido, las opciones disponibles son [ripio, dolarSi, coinmartcap]"
			raise ValueError(error_message)

	def get_test(self):
		return self.__source.get_test()


class Ripio():

	def __init__(self):
		print("Soy Ripio")
		self.test = 1

	def get_test(self):
		return self.test

class DolarSi():

	def __init__(self):
		print("Soy DolarSi")
		self.test = 2

	def get_test(self):
		return self.test

class CoinMarketCap():

	def __init__(self):
		print("Soy CoinMarketCap")
		self.test = 3

	def get_test(self):
		return self.test


ripio = cotizacion("s")

print(ripio.get_test())