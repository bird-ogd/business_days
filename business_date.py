import os
import json
from datetime import datetime, timedelta

f = open("bank_holidays.json")
content = f.read()
y = json.loads(content)

def is_business_day(date_string, day_type):
	if day_type == "c":
		return True
	split_date = date_string.split('-')
	date_delta = datetime(int(split_date[0]), int(split_date[1]), int(split_date[2])).weekday()
	if date_delta >= 5:
		return False	
	for k in y["england-and-wales"]['events']:
		if str(date_string) == k['date']:
			return False
	return True

def add_business_days(start_date, number, day_type):
	if day_type == "c":
		result_type = "calendar"
	else:
		result_type = "business"
	iter_date = start_date
	start_number = number
	while number > 1:
		if is_business_day(iter_date, day_type):
			number -= 1
		iter_date = datetime.strptime(iter_date, '%Y-%m-%d').date() + timedelta(days=1)
		iter_date = iter_date.strftime('%Y-%m-%d')
	print(str(start_number) + " " + result_type + " days after " + start_date + " = " + iter_date + " (inclusive of both dates)")

while True:
	date = input("Enter date: (yyyy-mm-dd) > ")
	day_type = input("Business days (b) or calendar days (c)? > ")
	number = float(input("Enter number of days > "))
	add_business_days(date, number, day_type)
	again = input("Again? Y/n > ")
	if again.lower() == "n":
		exit()