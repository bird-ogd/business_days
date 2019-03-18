import os
import json
from datetime import datetime, timedelta

f = open("bank_holidays.json")
content = f.read()
y = json.loads(content)

def is_business_day(date_string):
	split_date = date_string.split('-')
	date_delta = datetime(int(split_date[0]), int(split_date[1]), int(split_date[2])).weekday()
	if date_delta >= 5:
		return False	
	for k in y["england-and-wales"]['events']:
		if str(date_string) == k['date']:
			return False
	return True

def add_business_days(start_date, number):
	iter_date = start_date
	start_number = number
	while number > 1:
		if is_business_day(iter_date):
			number -= 1
			#print(iter_date)
		iter_date = datetime.strptime(iter_date, '%Y-%m-%d').date() + timedelta(days=1)
		iter_date = iter_date.strftime('%Y-%m-%d')
	print(str(start_number) + " business days after " + start_date + " = " + iter_date + " (inclusive of both dates)")

while True:
	date = input("Enter date: (yyyy-mm-dd) > ")
	number = float(input("Enter number of days > "))
	add_business_days(date, number)
	again = input("Again? Y/n > ")
	if again.lower() == "n":
		exit()