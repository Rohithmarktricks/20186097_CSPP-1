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
    for row in sudoku:
        if len(set(row)) == 9:
            return True
        return False

def check_column(sudoku):
    fun2 = zip(*sudoku)
    for row in fun2:
        if len(set(row)) == 9:
            return True
        return False

def check_matrix(sudoku):
    new = np.array(sudoku)
    a = new[0].reshape((3,3))
    b = new[1].reshape((3,3))
    c = new[2].reshape((3,3))
    d = new[3].reshape((3,3))
    e = new[4].reshape((3,3))
    f = new[5].reshape((3,3))
    g = new[6].reshape((3,3))
    h = new[7].reshape((3,3))
    i = new[8].reshape((3,3))

    final = np.concatenate((a[0],b[0],c[0]))
    final2 = np.concatenate((a[1],b[1],c[1]))
    final3 = np.concatenate((a[2],b[2],c[2]))
    final4 = np.concatenate((d[0],e[0],f[0]))
    final5 = np.concatenate((d[1],e[1],f[1]))
    final6 = np.concatenate((d[2],e[2],f[2]))
    final7 = np.concatenate((g[0],h[0],i[0]))
    final8 = np.concatenate((g[1],h[1],i[1]))
    final9 = np.concatenate((g[2],h[2],i[2]))

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
    if check_row(sudoku) and check_column(sudoku):
            if check_matrix(sudoku):
                return False
            return True
    


def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()