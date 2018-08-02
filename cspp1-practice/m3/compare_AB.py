'''
@author : Rohithmarktricks
This program compares two variables varA and varB
'''
VARA = int(input("Enter the VARA: "))
VARB = int(input("Enter the VARB: "))
if(isinstance(VARA, str) or isinstance(VARB, str)):
    print("Strings involved")
elif VARA > VARB:
    print("Bigger")
elif VARA == VARB:
    print("Equal")
else:
    print("Smaller")
