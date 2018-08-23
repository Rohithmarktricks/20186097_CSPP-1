import numpy as np
def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*m2)] for X_row in m1]


def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    add_mat = []
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        for i in m1:
            for j in i:
                    add_mat.append([i+j])
    return add_mat


def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    # s1 = input().split(",")
    # mat1 = []
    # for i in range(int(s1[0])+1):
    #     temp = input().split(" ")
    # for j in range(int(s1[0])):
    #     for k in range(int(s1[1])):
    #         mat1.append(int(temp[j][k]))
    # return mat1
    # mat = []
    #[rows, columns] = input().split(",")
    matrix_final = []
    list_input = input().split(",")
    rows, columns = int(list_input[0]), int(list_input[1])
    for i in range(rows):
        matrix = input().split(" ")
        if len(matrix) == columns:
            matrix_final.append([int(value) for value in matrix])
        else:
            print("Error!")
    return matrix_final, rows, columns

def main():
    # read matrix 1
    mat_1 = read_matrix()
    #new = []
    # order = len(mat_1)
    # for i in range(order):
    #     for j in range(order):
    #         new.append(map(int, mat_1[i][j]))

    mat_2 = read_matrix()
    #000000000000000000000000000000000000new_2 = []
    # order = len(mat_2)
    # for i in range(order):
    #     for j in range(order):
    #         new_2.append(map(int, mat_2[i][j]))

    #print(np.add(mat_1, mat_2))
    #print(new_2)
    #print(mat_1[0], mat_2[0])

    

    # read matrix 2

    # add matrix 1 and matrix 2
    print(add_matrix(mat_1, mat_2))

    # multiply matrix 1 and matrix 2
    print(mult_matrix(mat_1, mat_2))

if __name__ == '__main__':
    main()
