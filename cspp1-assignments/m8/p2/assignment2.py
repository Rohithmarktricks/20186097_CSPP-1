'''
Exercise: Assignment-2
Write a Python function, sumofdigits, that takes
in one number and returns the sum of digits of given number.
This function takes in one number and returns one number.
@Author : Rohithmarktricks
'''


def sum_of_digits(n_int):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    if n_int == 0:
        return 0

    return n_int%10 + sum_of_digits(n_int//10)


def main():
    '''
    Main function that prints sum of digits of input number
    '''
    a_int = input()
    print(sum_of_digits(int(a_int)))

if __name__ == "__main__":
    main()
