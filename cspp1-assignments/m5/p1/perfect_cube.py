'''
Write a python program to find if the given number is a perfect cube or not
using guess and check algorithm

testcase 1
Input: 24389
Output: 24389 is a perfect cube

testcase 2
Input: 21950
Output: 21950 is not a perfect cube
@Author : Rohithmarktricks
'''
def main():
    '''
    This main function takes a number to check if 
    it is a perfect cube!
    '''
    input_num = int(input())
    for guess_value in range(abs(input_num)):
        if guess_value**3 >= input_num:
            break
    if guess_value**3 != input_num:
        print("{} is not a perfect cube".format(input_num))
    else:
        if input_num < 0:
            guess_value = -guess_value
        print("{} is a perfect cube".format(input_num))



if __name__ == "__main__":
    main()
