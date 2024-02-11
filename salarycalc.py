#!/usr/bin/env python3
#Salary Calculator v2.1
#Converts annual salary to a hourly rate and vice versa.
#TODO: add error handling for invalid input

#Print to ask for annual or hourly income and prompt for user input.
print("Would you like to convert from Annual Income or Hourly Income?\nPress A for Annual or H for Hourly.")
income_type = input()

# function to convert annual pay to hourly pay
def convert_annual_to_hourly(annual_rate):
	hourly_rate = float(annual_rate) /52 /40
	biweekly_rate = hourly_rate * 80
	return hourly_rate, biweekly_rate

# function to convert hourly pay to annual pay
def convert_hourly_to_annual(hourly_rate):
	annual_rate = float(hourly_rate) * 40 * 52
	biweekly_rate = annual_rate /12 /2
	return annual_rate, biweekly_rate

if income_type.lower() == "a":
	annual_rate = input("Please enter annual rate: ")
	hourly_rate, biweekly_rate = convert_annual_to_hourly(annual_rate)
	print(f"An annual salary of ${annual_rate} comes to ${hourly_rate:.2f} an hour.\nYour bi-weekly gross pay would be ${biweekly_rate:.2f}.")

elif income_type.lower() == "h":
    hourly_rate = input("Please enter hourly rate: ")
    annual_rate, biweekly_rate = convert_hourly_to_annual(hourly_rate)
    print(f"An hourly rate of ${hourly_rate} comes to ${annual_rate:.2f} annually.\nYour bi-weekly gross pay would be ${biweekly_rate:.2f}.")

else:
	print("Invalid entry. Please try again.")