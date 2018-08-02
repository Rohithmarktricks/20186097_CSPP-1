#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s.
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl',
#your program should print:
#Number of vowels: 5
def main():
    str_input = input()
    # the input string is in s
    # remove pass and start your code here
    str2_input = str_input.lower()
    count_str = 0
    for i in str2_input:
        if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            count_str = count_str+1
    print(count_str)


if __name__ == "__main__":
    main()
