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

	print final_list
	solution = random.sample(final_list, 1)
	print solution

	guess_counter = 4
	result_of_guess = []
	while game_over != True:
		if guess_counter > 0:
			user_guess = raw_input("Guess ( %i left)? ")
			result_of_guess, number of correct = wordCheck(user_guess)
			if result_of_guess == True:
				print "%i/%i correct"
				print "You Win!"
			else:


		else:
			game_over = True



gameBegin()