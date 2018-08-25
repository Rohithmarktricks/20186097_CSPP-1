'''
Write a python program to read multiple lines of text input and store the input into a string.
@author : Rohithmarktricks
'''

def main():
    '''
    Main function!
    '''
    num_lines = int(input())
    new_str = ''
    for i in range(num_lines):
        del i
        new_str = input()
        print(new_str)

if __name__ == '__main__':
    main()
