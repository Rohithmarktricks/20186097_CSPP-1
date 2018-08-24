'''
To find addition and multiplication of the given matrices
@author : Rohithmarktricks
'''

def generate_resultant_matrix(rows, columns):
    '''
    To generate the zeros of the resultant matrices.
    '''
    # res_matrix = [[0]*columns]*rows
    # return res_matrix
    return [[0 for i in range(columns)] for j in range(rows)]

def mult_matrix(matrix_1, matrix_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    #rows = len(matrix_1)
    #columns = len(matrix_2[0])
    #multi_matrix = generate_resultant_matrix(rows, columns)
    if len(matrix_1[0]) == len(matrix_2):
        return [[sum(a*b for a, b in zip(X_row, Y_col))for Y_col in zip(*matrix_2)] for X_row in matrix_1]
    else:
        print("Error: Matrix shapes invalid for mult")
        return None

def add_matrix(matrix_1, matrix_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    rows = len(matrix_1)
    columns = len(matrix_1[0])
    add_matrices = generate_resultant_matrix(rows, columns)
    if len(matrix_1) == len(matrix_2) and len(matrix_1[0]) == len(matrix_2[0]):
        for i in range(rows):
            for j in range(columns):
                add_matrices[i][j] = matrix_1[i][j] + matrix_2[i][j]
        return add_matrices
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
            print("Error: Invalid input for the matrix")
            return None
    return matrix

def main():
    '''
    Main Function
    '''
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
