#Exercise : how many
# write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary.


def how_many(**kwargs):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    L=[]
    for val in kwargs.values():
        if type(val) == list or type(val) == tuple:
            L.extend(list(val))
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
    temp = animals
    print(temp)
    print(how_many(**temp))

if __name__== "__main__":
    main()
