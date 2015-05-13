def display_hangman(number_of_wrong):
    if number_of_wrong == 1:
        print "  |"
    elif number_of_wrong == 2:
        print "  |"
        print "  0"
    elif number_of_wrong == 3:
        print "  |"
        print "  0"
        print "  |"
    elif number_of_wrong == 4:
        print "  |"
        print "  0"
        print "/ |"
    elif number_of_wrong == 5:
        print "  |"
        print "  0"
        print "/ | \\"
    elif number_of_wrong == 6:
        print "  |"
        print "  0"
        print "/ | \\"
        print " /"
    else:
        print "  |"
        print "  0"
        print "/ | \\"
        print " / \\"            

input_word = raw_input("Please enter a word to be guessed \nthat does not contain ? or white space: ")

number_of_guesses = 0
q = list("?" * len(input_word))
while number_of_guesses < 7:
    guess = raw_input("Enter a guess letter: ")
    char_list = enumerate(list(input_word))
    for element in char_list:
        if guess == element[1]:
            q.pop(element[0])
            q.insert(element[0], guess)
            number_of_guesses += 1
        else:
            number_of_guesses += 1
            pass
    print q
    y = "".join(q)
    if y.isalpha():
        print "Done"

            




    
    




