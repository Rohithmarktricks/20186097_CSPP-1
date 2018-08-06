'''Exercise: fourth power
Write a Python function, fourthPower, that takes in one number and
returns that value raised to the fourth power.
You should use the square procedure that you defined in an earlier exercise
(you don't need to redefine square in this box_int;
This function takes in one number and returns one number.
@Author : Rohithmarktricks
'''
# To use the square file that you have created in the last exercise.
# You have to import the entire file or the function.
# In our case we will import entire file
import square as sq
# 'sq' will be used as an object to call the function of the square.py file
def square(x_int):
    '''
    x_int: int or float.
    '''
    return sq.square(x_int)


def fourth_power(x_int):
    '''
    x_int: int or float.
    '''
    return square(square(x_int))

def main():
    '''
    Main function takes in the number as a string and returns the
    fourth power of that number.
    '''
    data_input = input()
    data_input = float(data_input)
    temp = str(data_input).split('.')
    if temp[1] == '0':
        print(fourth_power(int(float(str(data_input)))))
        #print(square(int(float(str(data_input)))))
    else:
        print(fourth_power(data_input))


if __name__ == "__main__":
    main()
