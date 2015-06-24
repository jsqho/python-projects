def monthToNum(month):
	if month == 'Jan':
		return "01"
	elif month == 'Feb':
		return "02"
	elif month == 'Mar':
		return "03"
	elif month == "Apr":
		return "04"
	elif month == "May":
		return "05"
	elif month == "Jun":
		return "06"
	elif month == "Jul":
		return "07"
	elif month == "Aug":
		return "08"
	elif month == "Sep":
		return "09"
	elif month == "Oct":
		return "10"
	elif month == "Nov":
		return "11"
	elif month == "Dec":
		return "12"

def checkDayNumOneToNine(date_num):
	if date_num == "1":
		return "01"
	elif date_num == "2":
		return "02"
	elif date_num == "3":
		return "03"
	elif date_num == "4":
		return "04"
	elif date_num == "5":
		return "05"
	elif date_num == "6":
		return "06"
	elif date_num == "7":
		return "07"
	elif date_num == "8":
		return "08"
	elif date_num == "9":
		return "09"
	else:
		return date_num


def convertString(last_name, first_name, date):
	# This formats the Last Name
	if len(last_name) > 10: 			 #Check if last_name length is more than 10.
		temp_last_name = last_name[0:10] #If so, only take the first 10 characters.
	else:
		temp_last_name = last_name[0:len(last_name)] #If it's less than 10 characters,
		if len(temp_last_name) < 10:				 #Only take those characters.
			while len(temp_last_name) != 10:		 #And add "-" to them until the length is 10.
				temp_last_name = temp_last_name + "-"

	#This formats the First Name
	#This part works just like the Last Name Section
	if len(first_name) > 10:
		temp_first_name = first_name[0:10]
	else:
		temp_first_name = first_name[0:len(first_name)]
		if len(temp_first_name) < 10:
			while len(temp_first_name) != 10:
				temp_first_name = temp_first_name + "-"

	#This formats the Date
	date_string = date.split() #Break up the date input string.
	date_month = date_string[0][0:3] #Take only the Month.
	month_num = monthToNum(date_month) #Convert it to the month's number.
	day_num = date_string[1].rstrip(",") #Take the day number and remove the comma.
	new_day_num = checkDayNumOneToNine(day_num) #Add a zero to the front of numbers 1-9.
	year_num = date_string[2][2:] #Only take the last 2 digits of the year.

	converted_date = month_num + "/" + new_day_num + "/" + year_num # Put the date together.

	print ("Storing: "+ temp_last_name + temp_first_name + converted_date) # Concat all the results and print!


first_name = input("Please enter the student's first name: ")
last_name = input("Please enter the student's last name: ")
date = input("Please enter the student's enrollment date: ")
convertString(last_name, first_name, date)