'''
Exercise: PowerIter
Write a Python function, iterPower(base, exp),
that takes in two numbers and returns the base^(exp)
of given base and exp.
This function takes in two numbers and returns one number.
@Author : Rohithmarktricks
'''

def iter_power(base_int, exp_int):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    res_int = base_int
    while exp_int > 1:
        res_int *= base_int
        exp_int -= 1
    return res_int

def main():
    '''
    Main function
    '''

    data_int = input()
    data_int = data_int.split()
    print(iter_power(float(data_int[0]), int(data_int[1])))

if __name__ == "__main__":
    main()
