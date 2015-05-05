grade_list_tuples = []


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
				break
			else:
				grade_list_tuples.append([name,grade])
				break


#Option 2. Done
def remove_student():
	name_of_student = raw_input("Enter a name to be removed (Ex. Bob): ")
	for name_grade in grade_list_tuples:
		if name_of_student == name_grade[0]:
			grade_list_tuples.remove(name_grade)
			break
		else:
			pass


#Option 3. Done
def show_in_alpha_order():
	sorted_grade_list = sorted(grade_list_tuples)
	print "\n-----Displaying Grades-----"
	for name_grade in sorted_grade_list:
		print name_grade[0] + " : " + name_grade[1]
	print "-----Done Displaying Grades-----\n"


#Option 4. Done.
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

	mode_list = []
	for name_grade in grade_list_tuples:
		mode_list.append(name_grade[1])
	mode = max(set(mode_list), key=mode_list.count)

	print "\n-----Displaying Statistics-----"
	print "Mean : %i" % mean
	print "Median: " + median
	print "Mode: " + mode
	print "-----Done Displaying Statistics-----\n"
