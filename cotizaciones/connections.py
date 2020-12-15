from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


class ConnectionAPI():


	def connect_url(self, url, header, parameters):

		session = Session()
		session.headers.update(header)

		try:
			response = session.get(url, params=parameters)

		except (ConnectionError, Timeout, TooManyRedirects) as e:
			print(e)
			return False
