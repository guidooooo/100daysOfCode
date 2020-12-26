from calendar import Calendar
from datetime import datetime


def update_calendar_csv():

	try:
		init_year = 2017
		final_year = datetime.now().year + 2

		lst_dates = []

		for y in range(init_year, final_year):

			cal = Calendar(firstweekday=6).yeardatescalendar(y)

			for c in cal:
				#print(c.strftime("%Y-%m-%d"))
				for c1 in c:
					for c2 in c1:
						for c3 in c2:
							lst_dates.append(c3)


		final_lst = sorted(list(set(lst_dates)))
		#print(final_lst)


		with open('calendar.csv','w') as file:
			for line in final_lst:
				file.write(f"{line}\n")

		return True
		
	except:
		return False