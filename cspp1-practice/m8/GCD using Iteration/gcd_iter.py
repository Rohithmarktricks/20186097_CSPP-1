'''
Exercise: GCDIter
Write a Python function, gcdIter(a, b), that takes in two numbers
and returns the GCD(a,b) of given a and b.
This function takes in two numbers and returns one number.
@Author : Rohithmarktricks
'''

def gcd_iter(a_int, b_int):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a_int > b_int:
        min_int = b_int
    else:
        min_int = a_int
    hcf_int = 1
    for i in range(1, min_int+1):
        if ((a_int%i == 0) and (b_int%i == 0)):
            hcf_int = i
    return hcf_int

def main():
    '''
    Main function
    '''
    data_int = input()
    data_int = data_int.split()
    print(gcd_iter(int(data_int[0]), int(data_int[1])))

if __name__ == "__main__":
    main()
