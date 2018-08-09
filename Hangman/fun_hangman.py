import random

word_list_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(word_list_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print("  ", len(word_list), "words loaded.")
    return word_list

def choose_word(word_list):
   
    return random.choice(word_list)

word_list = load_words()

def is_word_guessed(secret_word, letters_guessed):
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    str1 = ""
    for i in secret_word:
        if i not in letters_guessed:
            str1 += "_"
        else:
            str1 += i
    return str1

def get_available_letters(letters_guessed):
    letters_next = ""
    letters_available = 'abcdefghijklmnopqrstuvwxyz'
    for i in letters_available:
        if i not in letters_guessed:
            letters_next += i
    return letters_next

def hangman(secret_word):
    print("My guessed word has {} letters in it".format(len(secret_word)))
    print(secret_word)
    guess_num = 8
    cond = True
    test_str=""
    while cond:
        if guess_num <=1:
            print(secret_word)
            break
        letters_guessed = input("Supply one guess letters :")
        test_str += letters_guessed
        print(is_word_guessed(secret_word,test_str))
        print(get_guessed_word(secret_word,test_str))
        print(get_available_letters(test_str))
        # if test_str == secret_word:
        #     break
        # else:
        #     if test_str 
        guess_num -= 1
        print("Left guesses :{}".format(guess_num))

    if get_guessed_word == secret_word:
        print("Your guess is correct")
    if guess_num == 0:
        print(secret_word)

def main():
    secret_word = choose_word(word_list).lower()
    hangman(secret_word)


if __name__ == "__main__":
    main()