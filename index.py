import os
import datetime as dt
import json
from datetime import timedelta, date

f = open("bank_holidays.json")
content = f.read()
y = json.loads(content)

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def date_range(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

clear()

while True:
	number = 0
	workdays = []
	bh = []

	start = raw_input("Enter start date (dd-mm-yyyy) > ")
	if start.lower() == "q":
		exit()
	end = raw_input("Enter end date (dd-mm-yyyy) >  ")
	if end.lower() == "q":
		exit()
	
	start_date = dt.datetime.strptime(start, '%d-%m-%Y').date()
	end_date = dt.datetime.strptime(end, '%d-%m-%Y').date() + timedelta(days=1)

	for single_date in date_range(start_date, end_date):
		single = str(single_date)
		listit = single.split('-')
		datedelta = dt.datetime(int(listit[0]), int(listit[1]), int(listit[2])).weekday()
		if datedelta < 5:
			workdays.append(single)
			number += 1

	for k in y["england-and-wales"]['events']:
		for l in workdays:
			if l == k['date']:
				bh.append(l)

	number_of_days = len(workdays) - len(bh)
	print(str(number_of_days) + " business days (inclusive of the start and end date)")

