#!/usr/bin/env python3
#Salary Calculator v2.0
#Converts annual salary to a hourly rate and vice versa.

#Print to ask for annual or hourly income and prompt for user input.
print("Would you like to convert from Annual Income or Hourly Income?\nPress A for Annual or H for Hourly.")
income_type = input()

if income_type == "A" or income_type == "a":
	print("Please enter annual rate: ")
	annual_rate = input()
	hourly_rate = float(annual_rate) /52 /40
	limit_hr = round(hourly_rate,2)
	biweekly_rate = limit_hr * 80
	print("An annual salary of $" + str(annual_rate) + " comes to $" + str(limit_hr) + " an hour.\nYour bi-weekly gross pay would be $" + str(biweekly_rate) + ".")
	quit()

if income_type == "H" or income_type == "h":
	print("Please enter hourly rate: ")
	hourly_rate = input()
	annual_rate = float(hourly_rate) * 40 * 52
	limit_ar = round(annual_rate,2)
	biweekly_rate = limit_ar /12 /2
	print("An hourly rate of $" + str(hourly_rate) + " comes to $" + str(limit_ar) + " annually.\nYour bi-weekly gross pay would be $" + str(biweekly_rate) + ".")
	quit()
	
else:
	print("Invalid entry for Income Type. Please try again.")
	quit()
