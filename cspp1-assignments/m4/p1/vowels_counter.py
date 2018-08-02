#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s.
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl',
#your program should print:
#Number of vowels: 5
'''
@author : Rohithmarktricks
This programs counts the number of vowels in the string.
'''
def main():
    '''
    This main function looks for vowels in the string using for loop and if condition.
    '''
    str_input = input()
    str2_input = str_input.lower()
    count_str = 0
    for i in str2_input:
        if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            count_str = count_str+1
    print(count_str)


if __name__ == "__main__":
    main()
