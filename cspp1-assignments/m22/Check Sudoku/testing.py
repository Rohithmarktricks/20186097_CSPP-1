'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    for i in sudoku:
        for j in i:
            if j not in "12345678910":
                return False
    return True
def count_number(sudoku):
    transpose = zip(*sudoku)
    for i in sudoku:
        for j in i:
            if i.count(j) != 1 and i.count(j) >= 1:
                return False
    for i1 in transpose:
        for j1 in i1:
            if i1.count(j1) != 1 and i1.count(j1) >= 1:
                return False
    return True

# def final_check(sudoku):
#     for i in sudoku:
#         for j in i:
#             if i.count(j) >= 1:
#                 return False
#     return True            

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''

    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for _ in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    actual_sudoku = sudoku
    input1 = check_sudoku(sudoku)
    # call solution function and print result to console
    if input1 is True:
        print(count_number(actual_sudoku))
    input2 = count_number(actual_sudoku)
    # if input2 is True:
    #     print(final_check(actual_sudoku))

if __name__ == '__main__':
    main()
