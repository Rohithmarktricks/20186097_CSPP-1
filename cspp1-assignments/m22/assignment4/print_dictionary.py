'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''
key = []
def print_dictionary(dictionary):
    '''
    print_dictionary function
    '''
    for keys in dictionary.items():
        key.append(keys)
        
    key.sort()
    for i in range(len(key)):
        print(str(key[i][0])+' - '+str(key[i][1]))


def main():
    '''
    Main function
    '''
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
