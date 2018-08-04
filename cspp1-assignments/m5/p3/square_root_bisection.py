'''
Write a python program to find the square root of the given num_intber
using approximation method
@author : Rohithmarktricks
'''

def main():
    '''
    This main function calculates the square root of num_int
    using Bisection method.
    '''
    num_int = int(input())
    # epsilon_value and step_value are initialized
    # don't change these values
    epsilon_value = 0.01
    step_value = 0.1
    # your code starts here
    init_value = 0.0
    last_value = num_int
    guess_value = (init_value + last_value)/2
    while abs(guess_value**2 - num_int) >= epsilon_value:
        if guess_value**2 < num_int:
            init_value = guess_value
        else:
            last_value = guess_value
        guess_value = (last_value + init_value)/2.0
    print(guess_value)


if __name__ == "__main__":
    main()
