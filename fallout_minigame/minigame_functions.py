import random

def chooseYourDifficulty():
	difficulty = int(raw_input("Difficulty (1-5)? "))
	if difficulty > 0 and difficulty <= 5:
		return str(difficulty)
	else:
		return "Invalid Difficulty."

def formatInputList(words):
	new_words = []

	for word in words:
		word = word.rstrip()
		new_words.append(word)

	for word in new_words:
		if len(word) <= 3:
			new_words.remove(word)

	return new_words

def formatForGameplay(words, difficulty):
	formatted_list = []
	level_num = int(difficulty)
	level_tuples = [ [1,4], [2,5], [3,6], [4,7], [5,8] ]

	for pair in level_tuples:
		if pair[0] == level_num:
			for word in words:
				if len(word) == pair[1]:
					formatted_list.append(word)

	list_for_user = random.sample(formatted_list, 10)

	return list_for_user

def wordCheck(user_guess, solution_word):
	number_of_correct = 0
	result_of_guess = False
	for x in user_guess:
		if x in solution_word:
			number_of_correct = number_of_correct + 1

	return number_of_correct






