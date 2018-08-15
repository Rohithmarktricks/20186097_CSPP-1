'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
    @Author : Rohithmarktricks

'''
global_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6':6, '7':7, '8':8,\
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
    #global_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    face_values = []
    suit_values = []
    for letter in hand:
        face_values.append(global_dict[letter[0]])
        #sum_values.append(letter[1])
    face_values.sort()
    for i in range(len(face_values)-1):
        if face_values[i+1]-face_values[i] != 1:
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
    # suit_values= []
    # count = 0
    # for h in hand:
    #     suit_values.append(h[1])
    # ref_suit = suit_values[0]
    # for i in range(1,len(suit_values)):
    #     if ref_suit == suit_values[i]:
    #         count += 1
    # if count == len(suit_values):
    #     return True
    # return False
    suit_list = []
    sum_values = 0
    for i in hand:
        suit_list.append(i[1])
    for i in suit_list:
        sum_values += ord(i)
    if sum_values == 5*ord(i):
        return True
    return False

def is_four_a_kind(hand):
    '''
    Returns True if four cards in a hand are same!
    '''
    suit_list = []
    for i in hand:
        suit_list.append(global_dict[i[0]])
    new_suit_list = sorted(suit_list)
    a = list(set(new_suit_list))
    if new_suit_list[0] == new_suit_list[1] == new_suit_list[2]:
        return True
    elif new_suit_list[1] == new_suit_list[2] == new_suit_list[3]:
        return True
    elif new_suit_list[2] == new_suit_list[3] == new_suit_list[4]:
        return True
    # total = []
    # for j in range(len(a)):
    #     total.append(sum(s.count(a[j])for s in new_suit_list))
    # if (i==4 for i in total):
    #     return True
    # return False

def is_three_a_kind(hand):
    '''
    Returns True if 3 cards in a hand are same!
    '''
    suit_list = []
    for i in hand:
        suit_list.append(global_dict[i[0]])
    new_suit_list = sorted(suit_list)
    a = list(set(new_suit_list))
    if new_suit_list[0] == new_suit_list[1] == new_suit_list[2] == new_suit_list[3]:
        return True
    elif new_suit_list[1] == new_suit_list[2] == new_suit_list[3] == new_suit_list[4]:
        return True
    # total = []
    # for j in range(len(a)):
    #     total.append(sum(s.count(a[j])for s in new_suit_list))
    # if (i==3 for i in total):
    #     return True
    # return False


def is_one_pair(hand):
    '''
    Returns True if there is a pair of same cards in a hand!
    '''
    suit_list = []
    for i in hand:
        suit_list.append(global_dict[i[0]])
    new_suit_list = sorted(suit_list)
    a = list(set(new_suit_list))
    if len(new_suit_list) - len(a) == 1:
        return True
    return False

def is_two_pair(hand):
    '''
    Returns True if there are two pairs of same card in a hand!
    '''
    suit_list = []
    for i in hand:
        suit_list.append(global_dict[i[0]])
    new_suit_list = sorted(suit_list)
    a = list(set(new_suit_list))
    if len(new_suit_list) - len(a) == 2:
        return True
    return False

def is_full_house(hand):
    '''
    Returns True if there is a three_of_a_kind and one_pair in a hand
    '''
    if is_three_a_kind(hand) and one_pair(hand):
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
    if is_straight(hand) and is_flush(hand):
        return 8
    elif is_four_a_kind(hand):
        return 7
    elif is_full_house(hand):
        return 6
    elif is_flush(hand):
        return 5
    elif is_three_a_kind(hand):
        return 3
    elif is_two_pair(hand):
        return 2
    elif is_one_pair(hand):
        return 1
    else:
        return 4    

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
