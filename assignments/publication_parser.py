import sys

f = open("recent_publications.txt", "r")
file_opened = f.read()


file_split = file_opened.splitlines()
doi_list = []
for element in file_split:
	if "doi" in element:
		doi_list.append(element)


new_doi_list = []
for element in doi_list:
	x = element.splitlines()
	new_doi_list.append(x)

pure_doi = []
check_list = []
for element in new_doi_list:
	one_line = element[0]

	split_one = one_line.split()
	#print split_one
	for chunk in split_one:
		if "doi:" in chunk:
			if chunk == "doi:":
				temp = chunk + split_one[len(split_one) - 1 ]
				check_list.append(split_one[len(split_one) - 1 ])
				pure_doi.append(temp)
			else:
				pure_doi.append(chunk)
#print len(pure_doi)
set_1 = set(pure_doi)
final_1 = list(set_1)

checker = True
remainder = []
for element in check_list:
	if element in pure_doi:
		pass
	else:
		remainder.append(element)

final_list = final_1 + remainder


new_split = file_opened.split("$")

list_of_month_and_doi_1 = []
for element in set(final_1):
	for strings in new_split:
		if element in strings:
			list_of_month_and_doi_1.append([strings[:14], element])

#print list_of_month_and_doi_1

list_month_doi_2 = []
for element in set(remainder):
	for strings in new_split:
		if element in strings:
			list_month_doi_2.append([strings[:14], element])

#print list_month_doi_2

#print len(list_of_month_and_doi_1)
#print len(list_month_doi_2)

fin = list_of_month_and_doi_1 + list_month_doi_2
#print fin
fresh = []
for x in fin:
	a = x[0].rstrip("\r\rIn")
	b = x[1]
	fresh.append([a,b])


fresh_2 = []
for x in fresh:
	a = x[0].rstrip("\r\rAm")
	b = x[1]
	fresh_2.append([a,b])

fresh_3 = []
for x in fresh_2:
	a = x[0].rstrip("\r\rR")
	b = x[1]
	fresh_3.append([a,b])

fresh_4 = []
for x in fresh_3:
	a = x[0].rstrip("\r\rEvol")
	b = x[1]
	fresh_4.append([a,b])

for x in fresh_4:
	if x[1].startswith("doi"):
		pass
	elif  x[1].startswith("http"):
		y = x[1].lstrip("http://dx.doi.org/")
		x[1] = "doi:" + y
	else:
		x[1] = "doi:" + x[1]

tuple_1 = []
for x in fresh_4:
	tuple_1.append(tuple(x))

def getKey(item):
	return item[0]


final_tuple = sorted(tuple_1, key=getKey)
#print final_tuple
l = open("dates_and_dois.txt", "w")
for x in final_tuple:
	l.write(x[0] + ", " + x[1] + "\n")




