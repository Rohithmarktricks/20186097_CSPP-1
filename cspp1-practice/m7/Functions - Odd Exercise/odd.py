'''
Exercise: odd
Write a Python function, odd, that takes in one number and
returns True when the number is odd and False otherwise.
You should use the % (mod) operator, not if.
This function takes in one number and returns a boolean.
@Author : Rohithmarktricks
'''

def odd(x_int):
    '''
    x_int: int or float.
    returns: True if x_int is odd, False otherwise
    '''
    return x_int%2 != 0

def main():
    '''
    This main function takes input from user to check if it is odd!
    '''
    data_int = input()
    print(odd(int(data_int)))

if __name__ == "__main__":
    main()
