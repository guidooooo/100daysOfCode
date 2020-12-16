from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import os

class ConnectionAPI():


	def connect_url(self, url, header, parameters):

		session = Session()
		session.headers.update(header)

		try:
			response = session.get(url, params=parameters)
			return response

		except (ConnectionError, Timeout, TooManyRedirects) as e:
			print(e)
			return False


	def connectAPI(self, source):

		if source.lower() == "ripio":
			url, header, parameters = self.get_ripio_setting()
		elif source.lower() == "dolarsi":
			url, header, parameters = self.get_dolarsi_setting()
		elif source.lower() == "coinmarketcap":
			url, header, parameters = self.get_coinmarketcap_setting()
		else:
			raise ValueError("Source Inexistente")

		return self.connect_url(url, header, parameters)

	def get_ripio_setting(self):

		parameters = {}
		
		headers = {
			'Accepts': 'application/json',
		}

		url = 'https://app.ripio.com/api/v3/rates/?country=AR'

		return url, headers, parameters

	def get_dolarsi_setting(self):

		parameters = {}

		headers = {
			'Accepts': 'application/json',
		}

		url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'

		return url, headers, parameters

	def get_coinmarketcap_setting(self):

		parameters = {
		  'start':'1',
		  'limit':'1',
		  'convert':'USD'
		}

		coinmarketcap_API_KEY = os.getenv('COINMARKETCAP_USER')

		headers = {
		  'Accepts': 'application/json',
		  'X-CMC_PRO_API_KEY': coinmarketcap_API_KEY,
		}

		url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

		return url, headers, parameters