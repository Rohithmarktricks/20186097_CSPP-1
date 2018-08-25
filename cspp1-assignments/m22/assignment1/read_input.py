'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    num_lines = int(input())
    new_str = ''
    for i in range(num_lines):
    	new_str = input()
    	print(new_str)
    	print('')	


if __name__ == '__main__':
    main()
