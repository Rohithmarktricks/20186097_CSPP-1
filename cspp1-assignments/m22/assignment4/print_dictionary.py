'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''
KEY = []
def print_dictionary(dictionary):
    '''
    print_dictionary function
    '''
    for KEYs in dictionary.items():
        KEY.append(KEYs)

    KEY.sort()
    for i in range(len(KEY)):
        print(str(KEY[i][0])+' - '+str(KEY[i][1]))


def main():
    '''
    Main function
    '''
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
