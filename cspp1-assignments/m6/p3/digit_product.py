'''
Given a  number int_input, find the product of all the digits
example:
    input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    digi_prod = 1
    for i in range(len(str(int_input))):
        del i 
        k = int_input%10
        digi_prod = digi_prod * k
        int_input = int_input // 10
    print(digi_prod)

if __name__ == "__main__":
    main()
