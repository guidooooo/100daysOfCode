import json
from connections import ConnectionAPI


currencies_dict = {
	'BTC_ARS_EXC_BUY' : 'BTC_ARS_EXC_BUY',
	'BTC_ARS_EXC_SELL' : 'BTC_ARS_EXC_SELL',
	'BTC_USD_BUY' : 'BTC_USD_BUY',
	'USD_ARS_EXC_BUY' : 'USD_ARS_EXC_BUY',
	'USD_ARS_EXC_SELL' : 'USD_ARS_EXC_SELL',
	'USD_ARS_OFC_BUY' : 'USD_ARS_OFC_BUY',
	'USD_ARS_OFC_SELL' : 'USD_ARS_OFC_SELL',
	'USD_ARS_BLU_BUY' : 'USD_ARS_BLU_BUY',
	'USD_ARS_BLU_SELL' : 'USD_ARS_BLU_SELL',
	'BTC_ARS_OFC_BUY' : 'BTC_ARS_OFC_BUY',
	'BTC_ARS_OFC_SELL' : 'BTC_ARS_OFC_SELL',
	'BTC_ARS_BLU_BUY' : 'BTC_ARS_BLU_BUY',
	'BTC_ARS_BLU_SELL' : 'BTC_ARS_BLU_SELL',
}

# all_exchanges = ['ripio', 'ripioexchange', 'buenbit', 'satoshitango', 'criptofacil', 'cryptomkt', 'qubit', 'xapo']
all_exchanges = ['ripio', 'ripioexchange', 'buenbit', 'satoshitango', 'criptofacil']


class Exchange():

	def get_rates(self, exchanges = ['ripio']):

		rates_dict = {}

		if exchanges[0] == 'all':
			exchanges = all_exchanges

		for exchange in exchanges:
			response = ConnectionAPI().connectAPI("arg_exchanges", exchange)
			data = json.loads(response.text)

			btc_buy = float(data['ask'])
			btc_sell = float(data['bid'])

			rates_dict[exchange] = {currencies_dict['BTC_ARS_EXC_BUY'] : btc_buy, currencies_dict['BTC_ARS_EXC_SELL']: btc_sell}

		
		return rates_dict

class Ripio():

	def __init__(self):
		self.btc_buy = -1
		self.btc_sell = -1
		self.btc_variation = -1
		self.usd_buy = -1
		self.usd_sell = -1

	def get_rates(self):
		
		response = ConnectionAPI().connectAPI("ripio_api")
		data = json.loads(response.text)

		for row in data:
			if row['ticker'] == "BTC_ARS":
			
				self.btc_buy = float(row['buy_rate'])
				self.btc_sell = float(row['sell_rate'])
				self.btc_variation = float(row['variation'])

				rates_dict = {currencies_dict['BTC_ARS_EXC_BUY'] : self.btc_buy, currencies_dict['BTC_ARS_EXC_SELL']: self.btc_sell, "btc_variation": self.btc_variation}

				return rates_dict

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
				rates_dict = {currencies_dict['USD_ARS_OFC_BUY']: self.usd_oficial_buy_rate, currencies_dict['USD_ARS_OFC_SELL']: self.usd_oficial_sell_rate, currencies_dict['USD_ARS_BLU_BUY']: self.usd_blue_buy_rate, currencies_dict['USD_ARS_BLU_SELL']: self.usd_blue_sell_rate}
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
		return {currencies_dict['BTC_ARS_BLU_BUY']: self.btc_blue_buy_rate, currencies_dict['BTC_ARS_BLU_SELL']: self.btc_blue_sell_rate, currencies_dict['BTC_ARS_OFC_BUY']: self.btc_oficial_buy_rate, currencies_dict['BTC_ARS_OFC_SELL']: self.btc_oficial_sell_rate}

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
		self.__btc_usd_rate=-1

	def get_rates(self):
		
		response = ConnectionAPI().connectAPI("coinmarketcap")
		data = json.loads(response.text)
			
		self.__btc_usd_rate = float(data["data"][0]['quote']['USD']['price'])

		return {currencies_dict['BTC_USD_BUY']: self.__btc_usd_rate}

	def get_btc_usd(self):

		if self.__btc_usd_rate == -1:
			self.get_rates()

		return self.__btc_usd_rate


def calculateUsdRate(exchanges_rates, btc_usd_rate):

	for exchange in exchanges_rates.items():

		usd_buy = round(exchange[1]['BTC_ARS_EXC_BUY']/btc_usd_rate,4)
		usd_sell = round(exchange[1]['BTC_ARS_EXC_SELL']/btc_usd_rate,4)

		exchanges_rates[exchange[0]]['USD_ARS_EXC_BUY'] = usd_buy
		exchanges_rates[exchange[0]]['USD_ARS_EXC_SELL'] = usd_sell

	return exchanges_rates