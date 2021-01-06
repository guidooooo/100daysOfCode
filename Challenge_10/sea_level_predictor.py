import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress





def draw_plot():
    # Read data from file
	df = pd.read_csv('epa-sea-level.csv')    

    # Create scatter plot
	fig, ax = plt.subplots()
	df.plot.scatter(x = 'Year', y='CSIRO Adjusted Sea Level', ax=ax)
	#print(ax.get_children()[0].get_offsets())
	#ax.get_children()[0].get_offsets().data.tolist()

    # Create first line of best fit
	res = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])

	years_extended = np.arange(1880, 2050, 1)
	line = [res.slope*xi + res.intercept for xi in years_extended]

	plt.plot(years_extended, line)

    # Create second line of best fit
	df_2000 = df[df['Year']>= 2000]
	res = linregress(df_2000['Year'],df_2000['CSIRO Adjusted Sea Level'])
	years_extended = np.arange(2000, 2050, 1)
	line = [res.slope*xi + res.intercept for xi in years_extended]
	plt.plot(years_extended, line)

    # Add labels and title
	plt.ylabel("Sea Level (inches)")
	plt.xlabel("Year")
	plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
	plt.savefig('sea_level_plot.png')
	return plt.gca()

draw_plot()