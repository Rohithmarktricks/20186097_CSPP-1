'''
hand.py python program
'''
import random

class Hand(object):
    '''
    Hand class
    '''
    def __init__(self, n):
        '''
        Initialize a Hand.

        n: integer, the size of the hand.
        '''
        assert type(n) == int
        self.HAND_SIZE = n
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

        # Deal a new hand
        self.deal_new_hand()

    def deal_new_hand(self):
        '''
        Deals a new hand, and sets the hand attribute to the new hand.
        '''
        # Set self.hand to a new, empty dictionary
        self.hand = {}

        # Build the hand
        numVowels = self.HAND_SIZE // 3

        for i_val in range(numVowels):
            del i_val
            x = self.VOWELS[random.randrange(0, len(self.VOWELS))]
            self.hand[x] = self.hand.get(x, 0) + 1

        for i_val in range(numVowels, self.HAND_SIZE):
            del i_val
            x = self.CONSONANTS[random.randrange(0, len(self.CONSONANTS))]
            self.hand[x] = self.hand.get(x, 0) + 1

    def set_dummy_hand(self, handString):
        '''
        Allows you to set a dummy hand. Useful for testing your implementation.

        handString: A string of letters you wish to be in the hand. Length of this
        string must be equal to self.HAND_SIZE.

        This method converts sets the hand attribute to a dictionary
        containing the letters of handString.
        '''
        assert len(handString) == self.HAND_SIZE, "Length of handString ({0})\
        must equal length of HAND_SIZE ({1})".format(len(handString), self.HAND_SIZE)
        self.hand = {}
        for char in handString:
            self.hand[char] = self.hand.get(char, 0) + 1


    def calculate_len(self):
        '''
        Calculate the length of the hand.
        '''
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans

    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        hand_keys = sorted(self.hand.keys())
        for letter in hand_keys:
            for j_val in range(self.hand[letter]):
                del j_val
                output += letter
        return output

    def update(self, word):
        """
        Does not assume that self.hand has all the letters in word.


        Updates the hand: if self.hand does have all the letters to make
        the word, modifies self.hand by using up the letters in the given word.

        Returns True if the word was able to be made with the letter in
        the hand; False otherwise.

        word: string
        returns: Boolean (if the word was or was not made)
        """
        # Your code here
        count_ = 0
        for i_val in word:
            if i_val in self.hand and self.hand[i_val] > 0:
                count_ += 1
        if count_ == len(word):
            for i_val in word:
                self.hand[i_val] = word.split().count(i_val)
            return True
        else:
            return False

myHand = Hand(7)
print(myHand)
print(myHand.calculate_len())

myHand.set_dummy_hand('aazzmsp')
print(myHand)
print(myHand.calculate_len())

myHand.update('za')
print(myHand)
