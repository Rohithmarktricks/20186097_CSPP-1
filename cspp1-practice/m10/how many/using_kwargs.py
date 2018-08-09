'''
Exercise : how many
write a procedure, called how_many, which returns
the sum of the number of values associated with a dictionary.
@Author : Rohithmarktricks
'''


def how_many(**kwargs):

    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    L = []
    if kwargs is not None:
        for key,value in kwargs.iteritems():
            if type(value) == int or type(value) == float:
                L.append(value)
            elif type(value) == list or type(value) == tuple:
                L.extend(list(value))
    print(sum(L))

    

def main():
    '''
    Main Function.
    '''
    # aDict={}
    # s=input()
    # l=s.split()
    # if l[0][0] not in aDict:
    #     aDict[l[0][0]]=[l[1]]
    # else:
    #     aDict[l[0][0]].append(l[1])

    aDict = {1:'Hello', 2:97, 3:'ok', 4:0, 5:0, 6:0}    
    how_many(**aDict)


if __name__== "__main__":
    main()