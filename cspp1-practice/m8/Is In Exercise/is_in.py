'''
Exercise: Is In
Write a Python function, isIn(char_str, a_str), that takes in
two arguments a char_stracter and String and
returns the isIn(char_str, a_str) which retuns a boolean value.
This function takes in two arguments
char_stracter and String and returns one boolean value.
@Author : Rohithmarktricks
'''
def is_in(char_str, a_str):
    '''
    char_str: a single char_stracter
    a_str: an alphabetized string

    returns: True if char_str is in a_str; False otherwise
    '''
    if char_str == a_str[0]:
        return True
    elif len(a_str) == 1:
        return False
    else:
        return is_in(char_str, a_str[1:])



def main():
    '''Main Function!
    '''
    data_int = input()
    data_int = data_int.split()
    print(is_in((data_int[0][0]), data_int[1]))


if __name__ == "__main__":
    main()
