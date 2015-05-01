def wrap_around_check(char, shift):
	if char.islower():
		check_shift = ord(char) + int(shift)
		if check_shift > 122:
			zero_shift = check_shift - 122
			final_letter = chr(96 + zero_shift)
			return final_letter
		elif check_shift == 122:
			final_letter = "z"
			return final_letter
		else:
			final_letter = chr(ord(char) + int(shift))
			return final_letter

	else:
		#print "THIS IS THE CHAR: " + char
		check_shift = ord(char) + int(shift)
		#print "THIS IS THE check shift value: %i" % check_shift
		if check_shift > 90:
			#print "IN THE IF STATEMENT"
			zero_shift = check_shift - 90
			#print "THIS IS ZERO SHIFT: %i" % zero_shift
			final_letter = chr(64 + zero_shift)
			#print "HERE'S THE LETTER: " + final_letter
			return final_letter
		elif check_shift == 90:
			final_letter = "Z"
			return final_letter
		else:
			final_letter = chr(ord(char) + int(shift))
			return final_letter



def shift_string(sentence, shift):
	new_sentence = ""

	for char in sentence:
		if char.isalpha():
			new_char = wrap_around_check(char, shift)
			new_sentence = new_sentence + new_char
		else:
			new_sentence = new_sentence + char

	print new_sentence
	


sentence = raw_input("Please enter a string to be ciphered: ")

while True:
	try:
		shift = int(raw_input("Please enter a shift amount between 0 and 25: "))
		if 0 < shift < 25:
			shift_string(sentence, shift)
			break
	except ValueError:
		continue


