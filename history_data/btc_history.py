import requests
import json
import time
import datetime
import csv



symbol = 'BTC'
exchange='bitfinex'
after = str(int(time.mktime(datetime.datetime.strptime('2019-11-01', "%Y-%m-%d").timetuple())))
#print(after)

url = f'https://api.cryptowat.ch/markets/{exchange}/{symbol}usd/ohlc'


resp = requests.get(url, params={
        'periods': '86400',
        'after': after
    })

resp.raise_for_status()
data = resp.json()

with open('btc_history_date.csv', mode='w') as btc_file:

	btc_writer = csv.writer(btc_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	for row in data['result']['86400']:
		btc_writer.writerow(row)		

	