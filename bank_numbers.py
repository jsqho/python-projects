import sys

def inputToList(nums):
		index = []
		for x in nums:
			x = int(x)
			index.append(x)
		return index

def bannerNumbers(acct_number):
	#Digits to Reference From
    digits = [
        [" _ ", "| |", "|_|"]  # 0
        , ["   ", "  |", "  |"]  # 1
        , [" _ ", " _|", "|_ "]  # 2
        , [" _ ", " _|", " _|"]  # 3
        , ["   ", "|_|", "  |"]  # 4
        , [" _ ", "|_ ", " _|"]  # 5
        , [" _ ", "|_ ", "|_|"]  # 6
        , [" _ ", "  |", "  |"]  # 7
        , [" _ ", "|_|", "|_|"]  # 8
        , [" _ ", "|_|", " _|"]  # 9
    ]
    numbers = inputToList(acct_number)
    level = 0
    depth = 3
    while level < depth:
    	for x in numbers:
    		print(digits[x][level]),
    	print("\n"),
    	level = level + 1

input_1 = '000000000'
input_2 = '111111111'
input_3 = '490067715'

bannerNumbers(input_1)
bannerNumbers(input_2)
bannerNumbers(input_3)
