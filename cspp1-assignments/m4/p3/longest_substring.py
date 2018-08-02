'''
This program is to print the longest substring in alphabetical order.
@author : Rohithmarktricks
'''
def main():
    '''
    This main function prints the longest substring in alphabetical order.
    '''
    input_str = input()
    temp_str = ""
    print(len(input_str))
    for i,letter in list(enumerate(input_str)):
        sub_str = input_str[i]
        if i+1 < len(input_str):
            while input_str[i] < input_str[i+1]:
                i += 1
                sub_str += input_str[i]
        else:
            break;
            if len(sub_str) > len(temp_str):
                temp_str = sub_str
    print(temp_str)

if __name__== "__main__":
    main()
