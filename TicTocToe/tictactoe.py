ROWS = 3
COLUMNS = 3


def is_valid_input(list_):
        for i in list_:
            for j in i:
                if j not in 'x.o':
                    return False
                else:
                    return True

def is_valid_game(new_test):
    x_ns = 0
    o_ns = 0
    for row in new_test:
        x_ns += row.count('x')
        o_ns += row.count('o')
    if x_ns > 5 or o_ns > 5:
        print("invalid game")
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
                    if (check_test_x[0][0] == check_test_x[1][1] == check_test_x[2][2]) or\
                        (check_test_x[0][2] == check_test_x[1][1] == check_test_x[2][0]):
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
                    if (check_test_o[0][0] == check_test_o[1][1] == check_test_o[2][2]) or\
                        (check_test_o[0][2] == check_test_o[1][1] == check_test_o[2][0]):
                        return True
                    else:
                        return False
                                
    
def main():
    tictactoe = []
    for i in range(ROWS):
        tictactoe.append(input().split())
    test = is_valid_input(tictactoe)
    if test:
        if is_valid_game(tictactoe):
            if check_x(tictactoe):
                print('x')
            elif check_o(tictactoe):
                print('o')
    else:
        print("invalid input")
        quit()            

main()