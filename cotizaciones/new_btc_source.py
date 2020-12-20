import requests
import time
import datetime

exchange = 'bitfinex'
after='2020-12-18'
symbol = 'btc'


element = datetime.datetime.strptime(after,"%Y-%m-%d") 
tuple = element.timetuple() 
timestamp = str(time.mktime(tuple)).split('.')[0]


url = 'https://api.cryptowat.ch/markets/{exchange}/{symbol}usd/price'.format(symbol=symbol, exchange=exchange)

resp = requests.get(url, params={ 'periods': '3600', 'after': timestamp})
data = resp.json()
print(data)