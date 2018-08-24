'''
To declare the winner for the TicTocToe Game
@author : Rohithmarktricks
'''
ROWS = 3
COLUMNS = 3

def is_valid_input(list_):
    '''
    To check if the input is a valid input
    '''
    for i in list_:
        for j in i:
            if j not in 'x.o':
                return False
    return True

def is_valid_game(new_test):
    '''
    to check if it is a valid game
    '''
    x_ns = 0
    o_ns = 0
    for row in new_test:
        x_ns += row.count('x')
        o_ns += row.count('o')
    if x_ns > 5 or o_ns > 5:
        print("invalid game")
        return None
    return True

def check_variables(check_test, check_variable):
    '''
    To check whether variable 'x' or 'o' is present
    '''
    count_ = 0
    new = zip(*check_test)
    for row in check_test:
        if row[0] == check_variable and len(set(row)) == 1:
            count_ += 1
    if count_ == 1:
        return True
    else:
        for row in new:
            if row[0] == check_variable and len(set(row)) == 1:
                count_ += 1
    if count_ == 1:
        return True
    else:
        if (check_test[0][0] == check_test[1][1] == check_test[2][2] == check_variable) or\
            (check_test[0][2] == check_test[1][1] == check_test[2][0] == check_variable):
            return True
        else:
            return False
def main():
    '''
    Main function
    '''
    tictactoe = []
    for i in range(ROWS):
        del i
        tictactoe.append(input().split())
    test = is_valid_input(tictactoe)
    if test:
        if is_valid_game(tictactoe):
            if check_variables(tictactoe, 'x') and check_variables(tictactoe, 'o'):
                print('invalid game')
            elif check_variables(tictactoe, 'x'):
                print('x')
            elif check_variables(tictactoe, 'o'):
                print('o')
            else:
                print('draw')
    else:
        print("invalid input")
        quit()

main()
