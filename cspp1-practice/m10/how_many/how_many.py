#Exercise : how many
# write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary.


def how_many(animals):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    L=[]
    print(animals.values())
    for i in animals.values():
        if type(i) == list or type(i) == tuple:
            L.extend(list(i))
    return len(L)

    

def main():
    # aDict={}
    # s=input()
    # l=s.split()
    # if l[0][0] not in aDict:
    #     aDict[l[0][0]]=[l[1]]
    # else:
    #     aDict[l[0][0]].append(l[1])
        
    # print(how_many(aDict))
    animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
    animals['d'] = ['donkey']
    animals['d'].append('dog')
    animals['d'].append('dingo')
    print(how_many(animals))

if __name__== "__main__":
    main()
