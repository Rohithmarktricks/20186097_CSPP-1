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

def is_valid_game(new_test):
    x_ns = new_test.count('x')
    o_ns = new_test.count('o')
    if x_ns or o_ns > 5:
        print("Invalid Game")
        return None
    else:
        return True

def check_x(check_test_x):
    new = zip(*check_test_x)
    for row in check_test_x:
        if row[0] == 'x' and len(set(row)) == 1 :
            return True
        else:
            for row in new:
                if row[0] =='x' and len(set(row)) == 1:
                    return True
                else:
                    if (check_test_x[0][0] == check_test_x[1][1] == check_test_x[2][2] == 'x') or\
                        (check_test_x[0][2] == check_test_x[1][1] == check_test_x[2][0] == 'x'):
                        return True
                    else:
                        return False

def check_o(check_test_o):
    new = zip(*check_test_o)
    for row in check_test_o:
        if row[0] == 'o' and len(set(row)) == 1 :
            return True
        else:
            for row in new:
                if row[0] =='o' and len(set(row)) == 1:
                    return True
                else:
                    if (check_test_o[0][0] == check_test_o[1][1] == check_test_o[2][2] == 'o') or\
                        (check_test_o[0][2] == check_test_o[1][1] == check_test_o[2][0] == 'o'):
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


