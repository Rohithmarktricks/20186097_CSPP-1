'''
Guess My Number Exercise
@author : Rohithmarktrciks
'''
def main():
    '''
    This funciton will guess the number.
    '''
    print("Think of a number between 0 and 100!")
    init_value = 0
    last_value = 100
    guess_value = (init_value + last_value)//2
    print("Is your secret number {} ?".format(int(guess_value)))
    while True:
        req_value = input("Enter 'h' to indicate the guess is too high.\
            Enter 'l' to indicate the guess is too low.\
            Enter 'c' to indicate I guessed correctly :")
        if req_value == 'l':
            init_value = guess_value
            guess_value = (init_value+last_value)//2
            print("Is your secret number {} ?".format(int(guess_value)))
        elif req_value == 'h':
            last_value = guess_value
            guess_value = (init_value+last_value)//2
            print("Is your secret number {} ?".format(int(guess_value)))
        elif req_value == 'c':
            print("Game over. your secret number was {}".format(int(guess_value)))
            break
        else:
            print("Please choose a valid option for l, h and c")


if __name__ == "__main__":
    main()
