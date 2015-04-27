from minigame_functions import *

def gameBegin():

	game_start = False
	while game_start != True:
		level = chooseYourDifficulty()
		if level == "Invalid Difficulty ?":
			print level
			game_start = False
		else:
			game_start = True

	word_file = open("words.txt", "r")
	proper_list = formatInputList(word_file)
	final_list = formatForGameplay(proper_list, level)
	for word in final_list:
		print word.upper()

	solution = random.sample(final_list, 1)

	guess_counter = 4
	result_of_guess = []
	game_over = False

	while game_over != True:
		if guess_counter > 0:
			user_guess = raw_input("Guess ( %i left )? " % guess_counter)
			number_of_correct = wordCheck(user_guess, solution[0])
			if number_of_correct == len(solution[0]):
				print "%i/%i correct" % (number_of_correct, len(solution[0]))
				print "You Win!"
				game_over = True
			else:
				print str(number_of_correct) + "/%i correct." % len(solution[0])
				guess_counter = guess_counter - 1
				game_over = False

		else:
			game_over = True
			print "Game Over"



gameBegin()