#!/usr/bin/python
from riccio import isLeapYear

leap_years = [x for x in range(1900,2001) if isLeapYear(x)]
days_in_month_normal = [0, 31,28,31,30,31,30,31,31,30,31,30,31]
days_in_month_leap = [0, 31,29,31,30,31,30,31,31,30,31,30,31]

sundays = 0

#make the starting day a sunday
year = 1900
month = 7
day = 1

while year < 2001:
	day += 7
	days_in_month = days_in_month_normal
	if year in leap_years:
		days_in_month = days_in_month_leap	
	if day > days_in_month[month]:
		#if we overflow the number of days in the month
		day -= days_in_month[month] #re-adjust the day
		month += 1 # increment the month
	if month == 13:
		#if we overflow the months
		month = 1  #revert month to 1	
		year += 1  #increment the year
	if day == 1:
		sundays += 1 #if day is 1, then increment sunday count
	
print sundays
