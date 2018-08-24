ROWS = 3
COLUMNS = 3


def read_tictactoe():
    tictactoe = []
    for _ in range(ROWS):
        list_matrix_row = input().split(" ")
        for i in list_matrix_row:
            if i in 'x.o':
                tictactoe.append([i  for i in list_matrix_row])
            else:
                print("Invalid input")
                return None
    return tictactoe

def is_valid_game(tictactoe):
    x_ns = tictactoe.count('x')
    o_ns = tictactoe.count('o')
    if x_ns or o_ns > 5:
        print("Invalid Game")
        return None
    else:
        return True

def check_x(tictactoe):
    new = zip(*tictactoe)
    for row in tictactoe:
        if row[0] == 'x' and len(set(row)) == 1 :
            return True
        else:
            for row in new:
                if row[0] =='x' and len(set(row)) == 1:
                    return True
                else:
                    if (tictactoe[0][0] == tictactoe[1][1] == tictactoe[2][2] == 'x') or\
                        (tictactoe[0][2] == tictactoe[1][1] == tictactoe[2][0] == 'x'):
                        return True
                    else:
                        return False

def check_o(tictactoe):
    new = zip(*tictactoe)
    for row in tictactoe:
        if row[0] == 'o' and len(set(row)) == 1 :
            return True
        else:
            for row in new:
                if row[0] =='o' and len(set(row)) == 1:
                    return True
                else:
                    if (tictactoe[0][0] == tictactoe[1][1] == tictactoe[2][2] == 'o') or\
                        (tictactoe[0][2] == tictactoe[1][1] == tictactoe[2][0] == 'o'):
                        return True
                    else:
                        return False
                                
    
def main():
    test = read_tictactoe()
    if test is None:
        exit()
    if is_valid_game(test):
        if check_x(test):
            print('x')
        elif check_o(test):
            print('o')
    else:
        exit()


