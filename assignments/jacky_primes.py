def prime_checker(end_number):
	for number in range(2, end_number + 1):
		mod_counters = 0
		for x in range(1, end_number + 1):
			if number % x == 0:
				mod_counters = mod_counters + 1
		if mod_counters == 2:
			print number


while True:
	try:
		end_number = int(raw_input("Please enter an integer >=2: "))
		if end_number >= 2:
			prime_checker(end_number)
			break
	except ValueError:
		continue