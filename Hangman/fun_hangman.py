'''
Hangman game
@Author : Rohithmarktricks
'''
import random

WORD_LIST_FILENAME = "words.txt"

def load_words():
    '''
    This function will load the random word from words.txt
    '''
    print("Loading word list from file...")
    # inFile: file
    in_file = open(WORD_LIST_FILENAME, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    WORD_LIST = line.split()
    print("  ", len(WORD_LIST), "words loaded.")
    return WORD_LIST

def choose_word(WORD_LIST):
    '''
    This function chooses a word randomly from word_list
    '''
    return random.choice(WORD_LIST)

WORD_LIST = load_words()

# def is_word_guessed(secret_word, letters_guessed):
#     for i in secret_word:
#         if i not in letters_guessed:
#             return False
#     return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    This function will give an output
    in this form Ex:for Hello : __l_o
    '''
    str1 = ""
    for i in secret_word:
        if i not in letters_guessed:
            str1 += "_"
        else:
            str1 += i
    return str1

def get_available_letters(letters_guessed):
    '''
    This function will provide all the remaining letters
    the alphabets!
    '''
    letters_next = ""
    letters_available = 'abcdefghijklmnopqrstuvwxyz'
    for i in letters_available:
        if i not in letters_guessed:
            letters_next += i
    return letters_next

def hangman(secret_word):
    '''
    hangman is the Parent function which gets the information from user defined functions!
    '''
    avail_alpha = "abcdefghijklmnopqrstuvwxyz"
    print("My guessed word has {} letters in it".format(len(secret_word)))
    print(secret_word)
    guess_num = 8
    cond = True
    test_str = ""
    tester_final = ""
    while cond:
        if guess_num <= 1:
            print(secret_word)
            break
        letters_guessed = input("Supply one guess letters :")
        if letters_guessed in secret_word:
            print("That's a correct guess!")
            test_str += letters_guessed
            #print(is_word_guessed(secret_word,test_str))
            tester_final = get_guessed_word(secret_word, test_str)
            print(get_guessed_word(secret_word, test_str))
            avail_alpha = get_available_letters(test_str)
            print(get_available_letters(test_str))
            if tester_final == secret_word:
                print("Your guess is correct")
                break

        else:
            guess_num -= 1
            print("Sorry you have made a wrong guess!")
            print("Available choices from {}".format(avail_alpha))
            print("Left guesses :{}".format(guess_num))

        if guess_num == 0:
            print(secret_word)

def main():
    '''
    Main Function!
    '''
    secret_word = choose_word(WORD_LIST).lower()
    hangman(secret_word)


if __name__ == "__main__":
    main()
