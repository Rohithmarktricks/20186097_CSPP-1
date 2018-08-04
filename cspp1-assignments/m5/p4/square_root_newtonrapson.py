'''
Write a python program to find the square root of the given number
using approximation method

testcase 1
input: 25
output: 4.999999999999998

testcase 2
input: 49
output: 6.999999999999991
@author : Rohithmarktricks
'''
def main():
    '''
    This main function calculates the square root of the number
    using Newton Raphson method
    '''
    s_int = int(input())
    # epsilon and step are initialized
    # don't change these values
    epsilon_val = 0.01
    guess_value = s_int/2.0
    #Code starts here
    while abs(guess_value*guess_value - s_int) >= epsilon_val:
        guess_value = guess_value - ((guess_value**2) - s_int)/(2*guess_value)
    print(guess_value)

if __name__ == "__main__":
    main()
