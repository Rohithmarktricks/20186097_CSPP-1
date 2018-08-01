'''
@author : Rohithmarktricks
This program compares two variables varA and varB
'''
VAR_A = int(input())
VAR_B = int(input())
if (type(VAR_B) or type(VAR_A) == str):
    print("string involved")
elif int(VAR_A) >  int(VAR_B):
    print("Bigger")
elif int(VAR_A) == int(VAR_B):
    print("equal")
else:
    print("smaller")