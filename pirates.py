def answer(numbers):
	WIB = [0,]
	work = True
	counter = 1
	while work == True:
		next = numbers[WIB[-1]]
		if next in WIB:
			WIB.append(next)
			#fin = len(set(numbers))
			work = False
		else:
			counter = counter + 1
			WIB.append(next)
	return counter
	#return fin


numbers_1 = [1,0]
numbers_2 = [1,2,1]

print answer(numbers_1)
print answer(numbers_2)
