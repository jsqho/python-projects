input_1 = '000000000'
input_2 = '111111111'
input_3 = '490067715'

def bannerNumbers(acct_number):
	for x in acct_number:
		if x == "1":
			current_number = " | \n |"
			entry = entry + current_number
		elif x == "2":
			current_number = " _\n _|\n|_"
			entry = entry + current_number


	print entry

bannerNumbers("12")