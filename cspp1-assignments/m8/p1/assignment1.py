'''
Exercise: Assignment-1
Write a Python function, factorial(n), that takes in
one number and returns the factorial of given number.
This function takes in one number and returns one number.
@Author : Rohithmarktricks
'''

def factorial(n_int):
    '''
    n_int is positive Integer
    returns: a positive integer, the factorial of n.
    '''
    if n_int <= 1:
        return 1
    else:
        k = n_int*fact(n_int-1)
        return(k)
    


def main():
    a = input()
    print(factorial(int(a)))    

if __name__== "__main__":
    main()
