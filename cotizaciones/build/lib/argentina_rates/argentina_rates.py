import sources
import json

class Rates():

	def __init__(self, btc_exchanges = ['all']):

		self.__btc_exchanges = btc_exchanges


	def get_btc_rates(self):

		rates_dict = {}

		# Getting ARS BTC rates
		btc_arg_rates = sources.Exchange().get_rates(self.__btc_exchanges)

		# print(btc_arg_rates)

		# Getting USD BTC rates
		btc_usd_obj = sources.CoinMarketCap()
		btc_usd_rate = btc_usd_obj.get_rates()
		

		# Adding ARS USD according ARS-BTC rates
		btc_arg_rates = sources.calculateUsdRate(btc_arg_rates, btc_usd_obj.get_btc_usd())
		btc_arg_rates['CoinMarketCap'] = btc_usd_rate


		# Getting ARS USD rates
		dolar_rates = sources.DolarSi().get_rates()
		btc_arg_rates['dolar'] = dolar_rates

		return btc_arg_rates


# rate = Rates()

# rates = rate.get_btc_rates()

# # app_json = json.dumps(rates, indent=4, sort_keys=True)

# with open('data.txt', 'w') as outfile:
#     json.dump(rates, outfile)

    