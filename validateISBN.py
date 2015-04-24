def validateISBN(isbn):
	isbn_list = isbn.split("-")
	work_list = list("".join(isbn_list))
	
	if work_list[9] == "X":
		work_list[9] = "10"
	
	multiplicand = 10
	final_sum = 0

	for digit in work_list:
		final_sum += multiplicand * int(digit)
		multiplicand = multiplicand - 1

	if final_sum % 11 == 0:
		return True
	else:
		return False




print(validateISBN("0-7475-3269-9"))
print(validateISBN("1-5688-1111-X"))