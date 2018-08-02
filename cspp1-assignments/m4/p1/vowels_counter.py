#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
    STRT = input()
    # the input string is in s
    # remove pass and start your code here
    STRT2 = STRT.lower()
    COUNT = 0
    for I in STRT2:
        if(I == 'a' or I == 'e' or I == 'i' or I == 'o' or I == 'u'):
            COUNT = COUNT+1
    print("Number of vowels :",COUNT)


if __name__== "__main__":
    main()
