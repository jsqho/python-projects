simon_pattern = "RRGBRYYBGY"
user_pattern = "RRGBBRYBGY"


compare_list = []
counter = 0
user_score = 0

while counter < len(simon_pattern):
	if simon_pattern[counter] == user_pattern[counter]:
		user_score = user_score + 1
		counter = counter + 1
	else:
		counter = counter + 1

print "User Score: %i" % user_score


