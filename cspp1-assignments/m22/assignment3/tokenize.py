'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
@author : Rohithmarktricks
'''
import re
ADICT = {}
def tokenize(string):
    '''
    tokenize function!
    '''
    string = re.sub(r'[^\w\s]', ' ', string).split()
    for word in string:
        if word not in ADICT:
            ADICT[word] = 1
        else:
            ADICT[word] += 1
    return ADICT

def main():
    '''
    ,Main function
    '''
    num = int(input())
    for i in range(num):
        del i
        new = tokenize(input())
    print(new)
if __name__ == '__main__':
    main()
