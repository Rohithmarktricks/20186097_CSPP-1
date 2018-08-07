'''
Exercise: Assignment-1
Write a Python function, factorial(n), that takes in
one number and returns the factorial of given number.
This function takes in one number and returns one number.
@Author : Rohithmarktricks
'''

def facto_rial(n_int):
    '''
    n_int is positive Integer
    returns: a positive integer, the factorial of n.
    '''
    if n_int <= 1:
        return 1
    else:
        k = n_int*facto_rial(n_int-1)
        return k



def main():
    '''
    Main function accepts input and prints factorial
    '''
    a_int = input()
    print(facto_rial(int(a_int)))

if __name__ == "__main__":
    main()
