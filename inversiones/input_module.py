
import pandas as pd
import numpy as np
from datetime import datetime
import csv
from clean_screen import clear

csv_file_name = 'sample.csv'



def ingresarInversion():
#file_name = '~/Document/Coding/100daysOfCode/inversiones/user_details.csv'

	print(f"Usted a elegido insertar nueva inversion".center(100,'*'))

	# Ingreso de monto en ARS
	while True:
		try:
			monto_ars = input("Ingrese el monto en ARS o X para salir: ")
			
			if str(monto_ars).lower() == 'x' : return False
			if str(monto_ars).lower().strip() == '': continue

			monto_ars = float(monto_ars)
			break

		except ValueError:
			print("Por favor ingrese un monto valido")

	# Ingreso de monto en BTC
	while True:
		try:
			monto_btc = input("Ingrese el monto en BTC o X para salir: ")
			
			if str(monto_btc).lower() == 'x': return False

			monto_btc = float(monto_btc)
			break

		except ValueError:
			print("Por favor ingrese un monto valido")

	# Fecha Ingreso
	fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	#print(monto_ars, monto_btc, dateTimeObject)

	with open(csv_file_name, mode = 'a') as inversiones_file:
		inversiones_file.write(f"\n{fecha_ingreso},{monto_ars},{monto_btc}")


def eliminarInversion():

	print(f"Usted a elegido eliminar una inversion existente".center(100,'*'))

	buscarInversion()


def buscarInversion():

	while True:
		try:
			fecha_filtro = input("Ingrese año y mes en el formato YYYY-MM de la inversion que desea eliminar o ingrese X para salir: ")
			if str(fecha_filtro).lower() == 'x' : return False
			if str(fecha_filtro).lower().strip() == '': continue

			int(fecha_filtro[:4])
			int(fecha_filtro[5:7])

			if len(fecha_filtro[5:]) != 2 or int(fecha_filtro[5:]) >12 or int(fecha_filtro[5:])<1: raise ValueError()
			if fecha_filtro[4] != '-': raise ValueError()

			break

		except ValueError:
				print("Por favor ingrese una fecha valida")


	df = pd.read_csv(csv_file_name)

	#mask = df['fecha'].strftime("%Y-%m") == fecha_filtro
	clear()
	print(df[df["fecha"].str.contains(fecha_filtro)])

	

eliminarInversion()