def display_hangman(number_of_wrong):
    if number_of_wrong == 1:
        print "  |"
    elif number_of_wrong == 2:
        print "  |"
        print "  O"
    elif number_of_wrong == 3:
        print "  |"
        print "  O"
        print "  |"
    elif number_of_wrong == 4:
        print "  |"
        print "  O"
        print "/ |"
    elif number_of_wrong == 5:
        print "  |"
        print "  O"
        print "/ | \\"
    elif number_of_wrong == 6:
        print "  |"
        print "  O"
        print "/ | \\"
        print " /"
    elif number_of_wrong == 7:
        print "  |"
        print "  O"
        print "/ | \\"
        print " / \\"
    else:
        pass

def compare_list(list_1, list_2):
    result = set(list_1) & set(list_2)
    #print result
    if set(result) == set(list_1):
        return True
    else:
        return False
def main():
    input_word = raw_input("Please enter a word to be guessed \nthat does not contain ? or white space: ")
    print "\n" * 30

    number_of_guesses = 0
    number_of_wrong = 0
    number_of_not_equal = 0
    q = list("?" * len(input_word))
    char_list = list(input_word)
    display_q = ""
    guessed_chars = ""
    check_list = False

    while number_of_guesses < 7:
        print "".join(q)
        print "So far you have guessed: " + ", ".join(sorted(guessed_chars))
        guess = raw_input("Please enter you next guess: ")
        char_list_enum = enumerate(list(input_word))
        if guess in guessed_chars:
            print "You already guessed the character: " + guess
        elif guess == " " or guess == "?":
            print "Invalid Character Guess"
        else:
            if len(guess) > 1:
                print "You can only guess a single character."
            else:
                for element in char_list_enum:
                    if guess == element[1]:
                        q.pop(element[0])
                        q.insert(element[0], guess)
                    else:
                        if guess not in char_list:
                            number_of_wrong += 1
                            break
                guessed_chars = guessed_chars + guess
                display_hangman(number_of_wrong)
                number_of_guesses += 1
                check_list = compare_list(char_list, q)
                if check_list == True:
                    print "You correctly guessed the secret word: " + "".join(q)
                    break


main()
