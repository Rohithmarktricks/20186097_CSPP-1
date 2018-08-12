'''
Assignment-3
@author : Rohithmarktricks
'''
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    count = 0
    if word in word_list:
        for i in list(word):
            if i in hand:
                count += 1
    return bool(count == len(word))

def main():
    '''
    Main function to call the list and dictionary.
    '''
    word = input()
    n = int(input())
    adict = {}
    for i in range(n):
        del i
        data = input()
        l = data.split()
        adict[l[0]] = int(l[1])
    l2 = input().split()
    print(is_valid_word(word, adict,l2))

if __name__ == "__main__":
    main()
