'''Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
@author : Rohithmarktricks
'''
def main():
    '''
    This main funciton will take a string to check if it has 'bob' in it.
    '''
    test_str = input()
    count_str = 0
    for i, le_enum in list(enumerate(test_str)):
        if(test_str[i] == 'b' and test_str[i+1] == 'o' and test_str[i+2] == 'b'):
            count_str += 1
    print(count_str)

if __name__ == "__main__":
    main()
