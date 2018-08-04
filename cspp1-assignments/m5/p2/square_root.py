'''
# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991
@author : Rohithmarktricks
'''

def main():
    '''
    This main function calculates the approximation of squareroot 
    a number
    '''
    s_int = int(input())
    # epsilon and step are initialized
    # don't change these values
    epsilon_val = 0.01
    step_val = 0.1
    guess_val = 0.0
    while abs(guess_val**2 - s_int) >= epsilon_val and guess_val <= s_int:
        guess_val += step_val
    print(guess_val)

if __name__ == "__main__":
    main()
