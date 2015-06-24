def file_to_list(text_file):
	file_1 = open(text_file, "r")
	list_1 = file_1.readlines()

	one = [x.rstrip() for x in list_1]

	temp_1 = []
	for element in one:
		for letter in element:
			temp_1.append(letter)

	return list(enumerate(temp_1))

def main():
	first_file = raw_input("Enter the name of the first file: ")
	second_file = raw_input("Enter the name of the second file: ")
	first = file_to_list(first_file)
	second = file_to_list(second_file)

	for i in range(len(first)):
		if first[i][1] != second[i][1]:
			first_char = first[i][1]
			second_char = second[i][1]
			print "Mismatch at character %i %s != %s" % (i, first_char, second_char)
		else:
			pass

main()



