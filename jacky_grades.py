grade_list_tuples = [["John","85"],["Bob","90"], ["Josh", "87"]]


#OPTION 1. Done.
def add_modify_student_grade():
	input_string = raw_input("Enter name and points (Ex. 'Bob 95'): ")
	name, grade = input_string.split()
	if len(grade_list_tuples) == 0:
		grade_list_tuples.append([name,grade])
	else:
		for name_grade in grade_list_tuples:
			if name == name_grade[0]:
				name_grade[1] = grade
			else:
				grade_list_tuples.append([name,grade])
	print grade_list_tuples

#Option 2. Done
def remove_student():
	name_of_student = raw_input("Enter a name to be removed (Ex. Bob): ")
	for name_grade in grade_list_tuples:
		if name_of_student == name_grade[0]:
			grade_list_tuples.remove(name_grade)
		else:
			pass
	print grade_list_tuples

#Option 3. Done
def show_in_alpha_order():
	sorted_grade_list = sorted(grade_list_tuples)
	print "-----Displaying Grades-----"
	for name_grade in sorted_grade_list:
		print name_grade[0] + " : " + name_grade[1]
	print "-----Done Displaying Grades-----"

def class_stats():
	#Mean Calculation
	total_points = 0
	for name_grade in grade_list_tuples:
		total_points = total_points + int(name_grade[1])
	mean = total_points/len(grade_list_tuples)

	#Median Calculation
	points_list = []
	for name_grade in grade_list_tuples:
		points_list.append(name_grade[1])
	sorted_points_list = sorted(points_list)
	median = sorted_points_list[len(sorted_points_list)/2]
	print median


	
