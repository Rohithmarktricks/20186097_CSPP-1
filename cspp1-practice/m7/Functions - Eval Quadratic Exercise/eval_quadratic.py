'''
Exercise: eval quadratic
Write a Python function, evalQuadratic(a, b, c, x), that returns the value of the quadratic
a . x 2 + b . x + c
This function takes in four numbers and returns a single number.
@Author : Rohithmarktricks
'''

def eval_quadratic(a_1, b_1, c_1, x_1):
    '''
    This function returns the value of ax^2 + bx + c
    '''
    return a_1*(x_1**2) + b_1*x_1 + c_1

def main():
    '''
    This main module takes in the values of a,b,c,x as a string separated by space.
    '''
    data_input = input()
    data_input = data_input.split(' ')
    data_input = list(map(float, data_input))
    # print(data_input)
    n_len = range(len(data_input))
    for x_1 in n_len:
        temp_int = str(data_input[x_1]).split('.')
        if temp_int[1] == '0':
            data_input[x_1] = int(float(str(data_input[x_1])))
        else:
            data_input[x_1] = data_input[x_1]
    print(eval_quadratic(data_input[0], data_input[1], data_input[2], data_input[3]))

if __name__ == "__main__":
    main()
