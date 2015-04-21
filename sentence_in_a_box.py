test_input = "EVERYWHERE IS WITHIN WALKING DISTANCE IF YOU HAVE THE TIME"

def sentenceInABox(input):

	#Create Box for Sentence
	size_of_box = 7
	square_list = [["-" for x in range(size_of_box)] for x in range(size_of_box)]

	#Input into List
	input_list = "".join(input.split())

	#Enter input into Square.
	row = 0
	column = 0
	test_count = 0
	while row < size_of_box and column < size_of_box:
		square_list[row][column] = input_list[test_count]
		test_count = test_count + 1
		if column == 6:
			row = row + 1
			column = 0
		else:
			column = column + 1

	#print input_list
	print_count = 0
	for x in square_list:
		print x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6]

sentenceInABox(test_input)