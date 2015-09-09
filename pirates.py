def answer(numbers):
	WIB = [0,]
	work = True
	while work == True:
		next = [WIB[-1]]
		if next in WIB:
			WIB.append(next)
			fin = len(WIB) - 1
			work = False
			return fin
		else:
			WIB.append(next)

numbers_1 = [1,0]
#numbers_2 = [1,2,1]

print answer(numbers_1)
#print answer(numbers_2)
