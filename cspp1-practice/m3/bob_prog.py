'''
@author : Rohithmarktricks
This program is to look if the string "bob" and returns the count.
'''
TEST = input("Enter the string  :")
COUNT = 0
for I, LETTER in list(enumerate(TEST)):
    if (TEST[I] == 'b' and TEST[I+1] == 'o' and TEST[I+2] == 'b'):
        COUNT += 1
print(COUNT)
