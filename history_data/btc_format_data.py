import csv
import pandas as pd
import numpy as np

import sys
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

import os

import requests
import json
import time
from datetime import datetime

#google spreadsheet libraries
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# mongo connection
from pymongo import MongoClient
import config

# Files names
btc_price_hist_file = 'btc_history_date.csv'
usd_price_hist_file = "dolar_history.csv"


from shutil import copyfile

#from calendar_function import update_calendar_csv

###############################
### funcion que devuelve la info de la spreadsheet con las compras 
###############################

def get_btc_purchases():

	scope = ['https://spreadsheets.google.com/feeds',
	         'https://www.googleapis.com/auth/drive']


	json_path = os.getenv('GOOGLEJSON')

	credentials = ServiceAccountCredentials.from_json_keyfile_name('../../../pythontest-287600-bc8175120fd6.json', scope)


	gc = gspread.authorize(credentials)

	###############################
	### END google spreadsheet settings
	###############################
	pd.options.display.float_format = '{:.5f}'.format

	# Reading spreadsheet
	wks = gc.open("purchases_list").sheet1
	data = wks.get_all_values()
	headers = data.pop(0)

	df_spreadsheet = pd.DataFrame(data, columns=headers)

	df_spreadsheet['date'] = pd.to_datetime(df_spreadsheet['date'], format = '%Y-%m-%d')

	df_spreadsheet = df_spreadsheet.astype({"date": object, "ars": int, "btc": float})
	df_spreadsheet = df_spreadsheet.set_index('date')



	df_spreadsheet['btcars'] = df_spreadsheet['ars'] / df_spreadsheet['btc']


	return df_spreadsheet



###############################
### funcion que formatea la columna date de un dataframe a datetime
###############################

def pd_format_date_column(df):

	df['date'] = pd.to_datetime(df['date'], unit='s').apply(lambda x: x.date())
	return  df

###############################
### funcion que lee un archivo csv y lo pasa a un dataframe panda
###############################

def get_price_hist(currency):

	# Reading btc historical file
	file = get_file_name(currency)
	df = pd.read_csv(file)
	df = df[df.columns[0:2]]
	columns = ['date','price']
	df.columns = columns

	df = df.astype({"date": 'datetime64', "price": 'float'})
	
	df = df.set_index('date')

	df_btcusd = df.groupby(['date']).mean() 

	return df_btcusd


###############################
### funcion que devuelve el max index de un dataframe
###############################
def get_price_last_date(df):

	return df.index.max()


###############################
### funcion que trae info del valor del BTC desde la fecha pasada como parametro
###############################

def get_newest_btc_prices(from_date):

	symbol = 'BTC'
	exchange='bitfinex'
	#after = str(int(time.mktime(datetime.datetime.strptime(from_date, "%Y-%m-%d").timetuple())))
	after = str(int(time.mktime(from_date.timetuple())))
	#print(after)

	url = f'https://api.cryptowat.ch/markets/{exchange}/{symbol}usd/ohlc'
		
	try:
		resp = requests.get(url, params={
		        'periods': '86400',
		        'after': after
		    })

		data = resp.json()
		
		df = pd.DataFrame.from_dict(data)

		# getting api list
		lst_api = df.loc['86400'].loc['result']

		# getting just the data I need
		lst_prices = [x[0:2] for x in lst_api] 

		# getting index for the dataframe
		indexes = [x[0] for x in lst_api]

		df_api = pd.DataFrame(lst_prices,  columns = ['date','price'])

		# formating dataframe column
		df_api = df_api.astype({"date": int, "price": float})
		# casting timestamp column to date
		df_api = pd_format_date_column(df_api)
		# setting date as index
		df_api = df_api.set_index('date')

		return df_api

	except (ConnectionError, Timeout, TooManyRedirects) as e:
			sys.exit(e)

###############################
### funcion que trae info del valor del USD Blue desde la fecha pasada como parametro
###############################
def get_newest_usd_prices(from_date):

	lst_prices = []

	#after =  datetime. strptime(from_date, '%Y-%m-%d')
	after = from_date

	col = connectMongo()

	myquery = { "fuente": "Blue_dolarSi", "par": "USD-ARS", "fecha" : { "$gt": after} }

	for x in col.find(myquery):
  		lst_prices.append([x['fecha'], x['cotizacionCompra']])

	df_usd_prices = pd.DataFrame(lst_prices,  columns = ['date','price'])
	df_usd_prices = df_usd_prices.astype({"date": 'datetime64', "price": 'float'})

	df_usd_prices['date'] = df_usd_prices['date'].dt.round('D') 

	df_usd_prices = df_usd_prices.set_index('date')

	df_usd_prices = df_usd_prices.groupby(['date']).mean() 

	return df_usd_prices

def get_file_name(currency):

	if currency.upper() == 'BTC':
		return btc_price_hist_file
	elif currency.upper() == 'USD':
		return usd_price_hist_file
	else:
		return False


###############################
### funcion que actualiza el csv con los precios del BTC y USD_BLUE segun parametro currency
###############################
def update_price_hist(currency):

	# getting csv file into dataframe
	df_hist = get_price_hist(currency)

	#droping last 2 days from dataframe
	df_hist.drop(df_hist.tail(2).index,inplace=True) # drop last n rows

	# getting max_date loaded
	max_date = get_price_last_date(df_hist)

	#getting btc price since last 2 days til today
	if currency == 'BTC':
		df_api = get_newest_btc_prices(max_date)
		
	elif currency == 'USD':
		df_api = get_newest_usd_prices(max_date)
	
	df_final = pd.concat([df_hist, df_api])

	#backup the file before update it
	file = get_file_name(currency)
	backup_csv_file(file)
	
	#saving csv
	df_final.to_csv(file)

	return True

def backup_csv_file(file):
	
	return copyfile(file, file + '.bkp')

#########################
## funcion que se conecta a mongo y te devuelve la coleccion con las cotizaciones
#########################

def connectMongo():

	user = os.getenv('MONGOUSER')
	password = os.getenv('MONGOPW')
	dbname = os.getenv('MONGODB')
	clusterName = os.getenv('MONNGOCLUSTER')
	client = MongoClient(f"mongodb+srv://{user}:{password}@{clusterName}.pkjzy.mongodb.net/{dbname}?retryWrites=true&w=majority")

	database = "ripio"
	collection = "rates"

	db = client[database]
	col = db[collection]

	return col


def do_the_maths(update_fg = False):

	if update_fg:
		#actualizo el csv de fechas
		#update_calendar_csv()
		#actualizo el csv de btc price
		update_price_hist('BTC')
		#actualizo el csv de usd price
		update_price_hist('USD')



	df_spreadsheet = get_btc_purchases()
	df_usd = get_price_hist("USD")
	df_usd = df_usd.rename(columns={'price': 'usd_price'})
	df1 = df_spreadsheet.join(df_usd)

	df_btc = get_price_hist("BTC")
	df_btc = df_btc.rename(columns={'price': 'btc_price'})

	df2 = df1.join(df_btc, on='date', how="left")

	df2['usd_amount'] = df2['ars'] / df2['usd_price']

	print(df2)

	current_btc_price = float(df_btc.loc[df_btc.index.max()].values[0])

	btc_stock = df2['btc'].sum()

	print("Supuestos dolares:", df2['usd_amount'].sum()) 
	print("Actuales por conversion:", current_btc_price*btc_stock)


do_the_maths(True)

