'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord 
the user is to guess. This starts up an interactive game of Hangman between 
the user and the computer. Be sure you take advantage of the three helper functions, 
isWordGuessed, getGuessedWord, and getAvailableLetters, 
that you've defined in the previous part.
'''

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
def is_word_guessed(secret_word, letters_guessed):
        '''
        True if guessed word in secret_word
        '''
    for i in secret_word:
        if i not in letters_guessed:
           return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
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
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters_next = ""
    letters_available = 'abcdefghijklmnopqrstuvwxyz'
    for i in letters_available:
        if i not in letters_guessed:
            letters_next += i
    return letters_next

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("My guessed word has {} letters in it".format(len(secretWord)))
    guess_num = 8
    cond = True
    while cond:
        letters_guessed = input("Supply one guess letters :")
        print(is_word_guessed(secret_word,letters_guessed))
        print(get_guessed_word(secret_word,letters_guessed))
        print(get_available_letters(letters_guessed))
        guess_num -= 1
        print("Left guesses :{}".format(guess_num))

    if get_guessed_word == secret_word:
        print("Your guess is correct")
    if guess_num == 0:
        print(secret_word)



    

def main():
    '''
    Main function for the given program
    
    When you've completed your hangman function, uncomment these two lines
	and run this file to test! (hint: you might want to pick your own
	secretWord while you're testing)
	'''
	secret_word = chooseWord(wordlist).lower()
	hangman(secret_word)


if __name__ == "__main__":
    main()
