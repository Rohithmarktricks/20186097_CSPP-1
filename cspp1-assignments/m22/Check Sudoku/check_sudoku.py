'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''
import numpy as np
def check_row(sudoku):
    '''
    To check with rows of martix
    '''
    for row in sudoku:
        if len(set(row)) == 9:
            for i in row:
                if i in '123456789':
                    return True
                return False
        return False

def check_column(sudoku):
    '''
    to check with columns of matrix
    '''
    fun2 = zip(*sudoku)
    for row in fun2:
        if len(set(row)) == 9:
            for i in row:
                if i in '123456789':
                    return True
                return False
        return False

def check_matrix(sudoku):
    '''
    to check the 3x3 grid
    '''
    new = np.array(sudoku)
    a_arr = new[0].reshape((3, 3))
    b_arr = new[1].reshape((3, 3))
    c_arr = new[2].reshape((3, 3))
    d_arr = new[3].reshape((3, 3))
    e_arr = new[4].reshape((3, 3))
    f_arr = new[5].reshape((3, 3))
    g_arr = new[6].reshape((3, 3))
    h_arr = new[7].reshape((3, 3))
    i_arr = new[8].reshape((3, 3))

    final = np.concatenate((a_arr[0], b_arr[0], c_arr[0]))
    final2 = np.concatenate((a_arr[1], b_arr[1], c_arr[1]))
    final3 = np.concatenate((a_arr[2], b_arr[2], c_arr[2]))
    final4 = np.concatenate((d_arr[0], e_arr[0], f_arr[0]))
    final5 = np.concatenate((d_arr[1], e_arr[1], f_arr[1]))
    final6 = np.concatenate((d_arr[2], e_arr[2], f_arr[2]))
    final7 = np.concatenate((g_arr[0], h_arr[0], i_arr[0]))
    final8 = np.concatenate((g_arr[1], h_arr[1], i_arr[1]))
    final9 = np.concatenate((g_arr[2], h_arr[2], i_arr[2]))

    if len(final.flatten()) == 9:
        if len(final2.flatten()) == 9:
            if len(final3.flatten()) == 9:
                if len(final4.flatten()) == 9:
                    if len(final5.flatten()) == 9:
                        if len(final6.flatten()) == 9:
                            if len(final7.flatten()) == 9:
                                if len(final8.flatten()) == 9:
                                    if len(final9.flatten()) == 9:
                                        return True
                                    return False
                                return False
                            return False
                        return False
                    return False
                return False
            return False
        return False
    return False

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    if check_row(sudoku)and check_column(sudoku):
        if check_matrix(sudoku):
            return False
        return True
    return False


def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        del i
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()
