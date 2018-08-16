'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
    @Author : Rohithmarktricks

'''
GOBAL_DICT = {'2': 2, '3': 3, '4': 4, '5': 5, '6':6, '7':7, '8':8,\
'9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    for i in range(len(hand)-1):
        if hand[i+1]-hand[i] != 1:
            return False
    return True

def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    # This way can be used, but it will get more complicated.And you have to compare with different
    # suites like clubs, spades, hearts, diamonds.
    sum_values = 0
    i_suit = hand[0]
    for i_suit in hand:
        sum_values += ord(i_suit)
    if sum_values == 5*ord(i_suit):
        return True
    return False

def is_four_a_kind(hand):
    '''
    Returns True if four cards in a hand are same!
    '''
    # for i in range(len(hand)-3):
    #     if hand[i] == hand[i+1] == hand[i+2] == hand[i+3]:
    #         return True
    return len(set(hand)) == 2

def is_three_a_kind(hand):
    '''
    Returns True if 3 cards in a hand are same!
    '''
    # for i in range(len(hand)-2):
    #     if hand[i] == hand[i+1] == hand[i+2]:
    #         return True
    #     return False
    return len(set(hand)) == 3


def is_one_pair(hand):
    '''
    Returns True if there is a pair of same cards in a hand!
    '''
    if len(hand) - len(set(hand)) == 1:
        return True
    return False

def is_two_pair(hand):
    '''
    Returns True if there are two pairs of same card in a hand!
    '''
    if len(hand) - len(set(hand)) == 2:
        return True
    return False


def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    face_hand = []
    suit_hand = []
    for i in hand:
        face_hand.append(GOBAL_DICT[i[0]])
        suit_hand.append(i[1])
    face_hand.sort()
    suit_hand.sort()

    # if royal_flush(hand):
    #   return 10
    # card_rank = ['--23456789TJQKA'.index(c) for c,s in hand]
    # card_rank.sort()
    # card_rank.reverse()
    if is_straight(face_hand) and is_flush(suit_hand):#For checking stright_flush
        return 9#8
    elif is_three_a_kind(hand) and is_one_pair(hand):# For checking Full_house
        return 8#7
    elif is_flush(suit_hand):
        return 7#6
    elif is_straight(face_hand):
        return 6#5
    elif is_four_a_kind(face_hand):
        return 5#4
    elif is_three_a_kind(face_hand):
        return 4#3
    elif is_two_pair(face_hand):
        return 3#2
    elif is_one_pair(face_hand):
        return 2#1
    return 1 #,card_rank)#0

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    '''
    def high_card(hands):
        a = max(hands[0])
        b = max(hands[1])
        if a > b:
            return 11
        return 1

    temp_ = high_card(hands)
    if temp_ < max(hands, key=hand_rank):
        return max(hands, key=hand_rank)
    return temp_
    '''
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
