def removeVowels(input_string):
	letters = []
	for x in input_string:
		letters.append(x)

	for letter in letters:
		if letter == "a" or letter == "e":
			letters.remove(letter)
		elif letter == "i" or letter == "o":
			letters.remove(letter)
		elif letter == "u":
			letters.remove(letter)

	final_string = ""
	for leftovers in letters:
		final_string = final_string + leftovers

	print final_string

removeVowels("Hello")
