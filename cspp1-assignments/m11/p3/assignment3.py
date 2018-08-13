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
    new_hand = hand.copy()
    if word in word_list:
        for i in word:
            if i in new_hand and new_hand[i] > 0:
                count += 1
                new_hand[i] -= 1
    return bool(count == len(word))

def main():
    '''
    Main function to call the list and dictionary.
    '''
    word = input()
    n_int = int(input())
    adict = {}
    for i in range(n_int):
        del i
        data = input()
        l_list = data.split()
        adict[l_list[0]] = int(l_list[1])
    l_list_2 = input().split()
    print(is_valid_word(word, adict, l_list_2))

if __name__ == "__main__":
    main()
