'''
Exercise: GCDRecr
Write a Python function, gcdRecur(a, b), that takes
in two numbers and returns the GCD(a,b) of given a and b.
This function takes in two numbers and returns one number.
@Author : Rohithmarktricks
'''

def gcd_recur(a_int, b_int):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b_int != 0:
        gcd_recur(b_int, a_int%b_int)
        return b_int



def main():
    '''
    Main Function!
    '''
    data_int = input()
    data_int = data_int.split()
    print(gcd_recur(int(data_int[0]), int(data_int[1])))

if __name__ == "__main__":
    main()
