'''
Exercise: Assignment-4
We are now ready to begin writing the code that interacts with the player.
We'll be implementing the playHand function.
This function allows the user to play out a single hand.
First, though, you'll need to implement the helper calculateHandlen function,
which can be done in under five lines of code.
@author : Rohithmarktricks
'''

def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string int)
    returns: integer
    """
    sum_ = 0
    for iter_ in hand:
        sum_ += hand[iter_]
    return sum_

def main():
    '''
    Main function
    '''
    n_len = input()
    adict = {}
    for i in range(int(n_len)):
        del i
        data = input()
        l_list = data.split()
        adict[l_list[0]] = int(l_list[1])
    print(calculate_handlen(adict))

if __name__ == "__main__":
    main()
