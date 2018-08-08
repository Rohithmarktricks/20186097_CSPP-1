'''
Exercise : Function and Objects Exercise-1
Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 4, 8, 9]
@Author : Rohithmarktricks
'''

def apply_to_each(l_int, f_int):
    '''
    Function to calculate abs of elements!
    '''
    for i in range(len(l_int)):
        l_int[i] = f_int(l_int[i])
    print(l_int)

def main():
    '''
    Main function
    '''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    apply_to_each(list1, abs)

if __name__ == "__main__":
    main()
