def prepared_matrix():
    '''
    To create a sample matrix
    '''
    list_input = input().split(",")
    matrix = []
    rows, columns = int(list_input[0]), int(list_input[1])
    for row in range(rows):
        matrix_row_list = input().split()
        if columns == len(matrix_row_list):
            matrix.append([int(i) for i in matrix_row_list])
    return matrix,rows,columns

def generate_resultant_matrix(rows, columns):
    '''
    to create a resultant matrix
    '''
    return [[0 for i in range(columns)] for j in range(rows)]

def transpose_mat(matrix_):
    '''
    Method for transpose of a Matrix
    '''
    matrix = matrix_[0]
    rows = matrix_[1]
    columns = matrix_[2]
    final_transpose = generate_resultant_matrix(rows, columns)
    for i in range(rows):
        for j in range(columns):
            if i == j:
                final_transpose[i][j] = matrix[i][j]
            else:
                final_transpose[i][j] = matrix[j][i]
    return final_transpose

def main():
    '''
    Main Function
    '''
    initial = prepared_matrix()
    print(transpose_mat(initial))

if __name__ == '__main__':
    main()

