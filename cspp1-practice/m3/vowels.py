'''
@author : Rohithmarktricks
This program counts the number of vowels in the given string.
'''
STRT = input("Enter the string  :")
STRT2 = STRT.lower()
COUNT = 0
for I in STRT2:
    if(I == 'a' or I == 'e' or I == 'i' or I == 'o' or I == 'u'):
        COUNT = COUNT+1
print("Number of vowels :",COUNT)
