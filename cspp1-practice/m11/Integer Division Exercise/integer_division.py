'''
Exercise: Integer Division Exercise
Modify the code for integer_division so that this error does not occur.
@author: Rohithmarktricks
'''
count = 0
def integer_division(x_int, a_int):
    """
    x_int: a_int non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    global count
    while x_int >= a_int:
        count += 1
        x_int = x_int - a_int
    return count

def main():
    '''
    Main function that takes in integer
    '''
    data = input()
    data = data.split()
    print(integer_division(int(data[0]), int(data[1])))


if __name__ == "__main__":
    main()
