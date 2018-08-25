'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_row(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    for row in sudoku:
        for element in row:
            if element not in "12345678910":
                return False
    return True

def check_column(sudoku):
    transpose = zip(*sudoku)
    # for row in sudoku:
    #     for element in row:
    #         if row.count(element) != 1 and row.count(element) >= 1:
    #             return False
    for row1 in transpose:
        for element1 in row1:
            if row1.count(element1) != 1 and row1.count(element1) >= 1:
                return False
    return True

       

def main():
    '''
        main function to read input sudoku from console
        call check_row function and print the result to console
    '''

    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for _ in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    actual_sudoku = sudoku
    input1 = check_row(sudoku)
    # call solution function and print result to console
    if input1 is True:
        print(check_column(actual_sudoku))

if __name__ == '__main__':
    main()
