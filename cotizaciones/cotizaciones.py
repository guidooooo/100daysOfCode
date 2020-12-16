import json
from connections import ConnectionAPI

class Ripio():

	def __init__(self):
		self.btc_buy = -1
		self.btc_sell = -1
		self.btc_variation = -1
		self.usd_buy = -1
		self.usd_sell = -1

	def get_rates(self):
		
		response = ConnectionAPI().connectAPI("Ripio")
		data = json.loads(response.text)

		for row in data:
			if row['ticker'] == "BTC_ARS":
			
				self.btc_buy = float(row['buy_rate'])
				self.btc_sell = float(row['sell_rate'])
				self.btc_variation = float(row['variation'])

				rates_dict = {"btc_buy" : self.btc_buy, "btc_sell": self.btc_sell, "btc_variation": self.btc_variation}

				return rates_dict

	def calculateUsdRate(self, btc_rate):

		if self.btc_buy == -1 or self.btc_sell == -1:
			self.get_rates()

		btc_usd_rate = btc_rate.get_btc_usd()

		self.usd_buy = round(self.btc_buy/btc_usd_rate,4)
		self.usd_sell = round(self.btc_sell/btc_usd_rate,4)

		return {'usd_ripio_buy': self.usd_buy, 'usd_ripio_sell': self.usd_sell}

class DolarSi():

	def __init__(self):
		#Oficial
		self.usd_oficial_buy_rate=-1
		self.usd_oficial_sell_rate=-1
		#Blue
		self.usd_blue_buy_rate=-1
		self.usd_blue_sell_rate=-1
		#BTC al Oficial
		self.btc_oficial_buy_rate=-1
		self.btc_oficial_sell_rate=-1
		#BTC al Blue
		self.btc_blue_buy_rate=-1
		self.btc_blue_sell_rate=-1

	def get_rates(self):
		
		response = ConnectionAPI().connectAPI("DolarSi")
		data = json.loads(response.text)

		i = 0
		y = 0
		for row in data:
			if row['casa']['nombre'].lower().split()[1] == "oficial":
				self.usd_oficial_buy_rate = float(row['casa']['compra'].replace(",","."))
				self.usd_oficial_sell_rate = float(row['casa']['venta'].replace(",","."))
				i += 1
			if row['casa']['nombre'].lower().split()[1] == "blue":
				self.usd_blue_buy_rate = float(row['casa']['compra'].replace(",","."))
				self.usd_blue_sell_rate = float(row['casa']['venta'].replace(",","."))
				i += 1

			if i == 2:
				rates_dict = {"usd_oficial_buy_rate": self.usd_oficial_buy_rate, "usd_oficial_sell_rate": self.usd_oficial_sell_rate, "usd_blue_buy_rate": self.usd_blue_buy_rate, "usd_blue_sell_rate": self.usd_blue_sell_rate}
				return rates_dict

			y +=1
			if y>100: break

	def calculateBtcRate(self, btc_rate):

		# Me traigo la cotizacion BTC en USD
		btc_usd_rate = btc_rate.get_btc_usd()

		# Calculo cuantos pesos esta el BTC a cotizacion oficial
		self.btc_blue_buy_rate, self.btc_blue_sell_rate =  self.get_btc_blue_rates(btc_usd_rate)
		# Calculo cuantos pesos esta el BTC a cotizacion blue
		self.btc_oficial_buy_rate, self.btc_oficial_sell_rate = self.get_btc_blue_rates(btc_usd_rate)

		# Retorno diccionario con los valores calculados
		return {"btc_blue_buy_rate": self.btc_blue_buy_rate, "btc_blue_sell_rate": self.btc_blue_sell_rate, "btc_oficial_buy_rate": self.btc_oficial_buy_rate, "btc_oficial_sell_rate": self.btc_oficial_sell_rate}

	def get_btc_blue_rates(self, btc_usd_rate):

		btc_oficial_buy_rate = round(btc_usd_rate*self.usd_oficial_sell_rate,4)
		btc_oficial_buy_rate = round(btc_usd_rate*self.usd_oficial_buy_rate,4)

		return btc_oficial_buy_rate , btc_oficial_buy_rate

	def get_btc_oficial_rates(self, btc_usd_rate):

		btc_blue_buy_rate = round(btc_usd_rate*self.usd_blue_sell_rate,4)
		btc_blue_sell_rate = round(btc_usd_rate*self.usd_blue_buy_rate,4)

		return btc_blue_buy_rate , btc_blue_sell_rate


class CoinMarketCap():

	def __init__(self):
		self.btc_usd_rate=-1

	def get_rates(self):
		
		response = ConnectionAPI().connectAPI("coinmarketcap")
		data = json.loads(response.text)
			
		self.btc_usd_rate = float(data["data"][0]['quote']['USD']['price'])

		return {"btc_usd_rate": self.btc_usd_rate}

	def get_btc_usd(self):

		if self.btc_usd_rate == -1:
			dict_btc = self.get_rates()
			return dict_btc['btc_usd_rate']

		return self.btc_usd_rate

ripio = Ripio()
print(ripio.get_rates())
dolarsi = DolarSi()
print(dolarsi.get_rates())
coinMarket = CoinMarketCap()
print(coinMarket.get_rates())

print(ripio.calculateUsdRate(coinMarket))
print(dolarsi.calculateBtcRate(coinMarket))

