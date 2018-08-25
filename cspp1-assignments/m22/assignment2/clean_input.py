'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
@author : Rohithmarktricks
'''
import re
def clean_string(string):
    '''
    clean string Function!
    '''
    clean = re.sub('\\W+', '', string)
    return clean

def main():
    '''
    Main function
    '''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
