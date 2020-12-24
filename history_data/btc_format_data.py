import csv
import pandas as pd
import numpy as np

import sys
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

import requests
import json
import time
import datetime

#google spreadsheet libraries
import gspread
from oauth2client.service_account import ServiceAccountCredentials


###############################
### funcion que devuelve la info de la spreadsheet con las compras 
###############################

def get_btc_purchases():

	scope = ['https://spreadsheets.google.com/feeds',
	         'https://www.googleapis.com/auth/drive']

	credentials = ServiceAccountCredentials.from_json_keyfile_name('pythontest-287600-bc8175120fd6.json', scope)

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
### funcion que lee el .csv con el valor historico del btc
###############################

btc_price_hist_file = 'btc_history_date.csv'

def pd_format_date_column(df):

	df['date'] = pd.to_datetime(df['date'], unit='s').apply(lambda x: x.date())
	return  df

def get_btc_price_hist():

	# Reading btc historical file
	df = pd.read_csv(btc_price_hist_file)
	df = df[df.columns[0:2]]
	# #print(df)
	columns = ['date','price']
	df.columns = columns

	df = df.astype({"date": 'datetime64', "price": 'float'})
	
	df = df.set_index('date')

	df_btcusd = df.groupby(['date']).mean() 

	return df_btcusd


###############################
### funcion que devuelve la ultima fecha que tiene el csv de BTC_PRICE
###############################
def get_btc_price_last_date(df):

	return df.index.max()

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

		
		print(resp.raise_for_status())
		data = resp.json()
		return pd.DataFrame.from_dict(data)

	except (ConnectionError, Timeout, TooManyRedirects) as e:
			sys.exit(e)


	


###############################
### funcion que actualiza el csv con los precios del BTC
###############################
def update_btc_price_hist():

	# getting csv file into dataframe
	df_hist = get_btc_price_hist()

	#droping last 2 days from dataframe
	df_hist.drop(df_hist.tail(2).index,inplace=True) # drop last n rows

	# getting max_date loaded
	max_date = get_btc_price_last_date(df_hist)


	#getting btc price since last 2 days til today
	df_btc_api = get_newest_btc_prices(max_date)

	# getting api list
	lst_api = df_btc_api.loc['86400'].loc['result']

	# getting just the data I need
	lst_prices = [x[0:2] for x in lst_api] 

	# getting index for the dataframe
	indexes = [x[0] for x in lst_api]

	# creating dataframe from LST_PRICES
	df_btc_new_prices = pd.DataFrame(lst_prices,  columns = ['date','price'])
	# formating dataframe column
	df_btc_new_prices = df_btc_new_prices.astype({"date": int, "price": float})
	# casting timestamp column to date
	df_btc_new_prices = pd_format_date_column(df_btc_new_prices)
	# setting date as index
	df_btc_new_prices = df_btc_new_prices.set_index('date')

	df_final = pd.concat([df_hist, df_btc_new_prices])

	df_final.to_csv(btc_price_hist_file)


	return True

#update_btc_price_hist()

df_spreadsheet = get_btc_purchases()
df_btcusd = get_btc_price_hist()


print(df_spreadsheet.join(df_btcusd))


