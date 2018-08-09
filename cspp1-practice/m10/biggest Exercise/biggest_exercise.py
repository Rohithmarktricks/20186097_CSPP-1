'''
Exercise : Biggest Exercise
Write a procedure, called biggest, which returns the key corresponding to the entry with
the largest number of values associated with it. If there is more than one such entry,
return any one of the matching keys.
@author:Rohithmarktricks
'''

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    maxi = 0
    count = 0
    for i in aDict:
        if type(aDict[i]) == list or type(aDict[i]) == tuple:
            if len(aDict[i])>count:
                maxi = i
                count = len(aDict[i])
    return maxi, count 
        
def main():
    '''
    Main Function
    '''
    animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

    animals['d'] = ['donkey']
    animals['d'].append('dog')
    animals['d'].append('dingo')
        
    print(biggest(animals))
    
if __name__ == "__main__":
    main()