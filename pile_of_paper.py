import sys

def create_base_canvas(one_row_length, num_of_rows):
	base_sheet_list =[]
	one_row = "0" * one_row_length
	for x in range(num_of_rows):
		base_sheet_list.append(one_row)
	return base_sheet_list

def apply_sheets(color, start_row, start_column, width, height, base_sheet):
	color = str(color)
	while height > 0:
		row_to_be = list(base_sheet[start_row])
		for i in range(start_column, start_column + width):
			row_to_be[i] = color

		modded_row = "".join(row_to_be)
		base_sheet[start_row] = modded_row
		start_row += 1
		height = height - 1
	return base_sheet

def count_sheets(base_sheet):
	zeroes = 0
	ones = 0
	twos = 0
	for row in base_sheet:
		zeroes = zeroes + row.count("0")
		ones = ones + row.count("1")
		twos = twos + row.count("2")
	print "0 " + str(zeroes)
	print "1 " + str(ones)
	print "2 " + str(twos)

def main():
	base_sheet = create_base_canvas(20,10)
	first_apply = apply_sheets(1,5,5,10,3,base_sheet)
	second_apply = apply_sheets(2,0,0,7,7,base_sheet)
	count_sheets(second_apply)

main()
