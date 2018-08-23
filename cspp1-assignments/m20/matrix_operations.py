import numpy as np

def generate_resultant_matrix(rows, columns):
    # res_matrix = [[0]*columns]*rows
    # return res_matrix
    return [[0 for i in range(columns)] for j in range(rows)]

def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    rows = len(m1)
    columns = len(m2[0])
    multi_matrix = generate_resultant_matrix(rows, columns)
    if len(m1[0]) == len(m2[0]):
        result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*m2)] for X_row in m1]
        #pass
    else:
        print("Error: Matrix shpaes invalid for multi")
        return None
    
    

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    final = []
    rows = len(m1)
    columns = len(m1[0])
    add_matrix = generate_resultant_matrix(rows, columns)
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        for i in range(rows):
            for j in range(columns):
                add_matrix[i][j] = m1[i][j] + m2[i][j]
        return add_matrix
    else:
        print("Error: Matrix shapes invalid for addition")
        return None

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    matrix = []
    list_input = input().split(",")
    rows, columns = int(list_input[0]), int(list_input[1])
    for _ in range(rows):
        list_matrix_row = input().split()
        if columns == len(list_matrix_row):
            matrix.append([int(i) for i in list_matrix_row])
        else:
            print("Error!")
    return matrtix

def main():
    # read matrix 1
    mat_1 = read_matrix()
    if mat_1 is None:
        exit()
    mat_2 = read_matrix()
    if mat_2 is None:
        exit()

    print(add_matrix(mat_1, mat_2))

    print(mult_matrix(mat_1, mat_2))

if __name__ == '__main__':
    main()
