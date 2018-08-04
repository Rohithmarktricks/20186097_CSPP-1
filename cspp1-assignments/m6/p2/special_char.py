'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_input = input()
    char_input = '!@#$%^&*'
    for i, letter1 in list(enumerate(str_input)):
        del letter1
        for j, letter2 in list(enumerate(char_input)):
            del letter2
            if str_input[i] == char_input[j]:
                str_input = str_input[:i]+" "+str_input[i+1:]
    print(str_input)

if __name__ == "__main__":
    main()
