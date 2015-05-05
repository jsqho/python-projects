from grader_commands import *

while True:
	print "1. Add/modify student grade"
	print "2. Delete student grade"
	print "3. Print student grades"
	print "4. Display the course statistics"
	print "5. Quit"
	user_choice = raw_input("Your choice: ")
	if user_choice == "1":
		add_modify_student_grade()

	elif user_choice == "2":
		remove_student()

	elif user_choice == "3":
		show_in_alpha_order()

	elif user_choice == "4":
		class_stats()

	elif user_choice == "5":
		break

	else:
		print "Unrecognized Command"
