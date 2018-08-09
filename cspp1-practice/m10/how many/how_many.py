'''
Exercise : how many
write a procedure, called how_many, which returns
the sum of the number of values associated with a dictionary.
@Author : Rohithmarktricks
'''


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    for i in range(len(aDict.values())):
        if type(i) == list or type(i) == tuple:
            return L.extend(i)
        elif type(i) == int or list(i) == float:
            return L.append(i)

    

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
    print(how_many(aDict))


if __name__== "__main__":
    main()