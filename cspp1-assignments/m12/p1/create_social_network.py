'''
    Assignment-1 Create Social Network
'''
print_social = {}
lines = 0
def create_social_network(data):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''
    # j = 0
    # for i in range(lines):
    #     print(i)
    #     final_data[i] = data[i].split()
    #     print(data[i])
    #     if final_data[i][j] not in print_social:
    #         print_social[j] = final_data[j+2]
    #     j += 1
    # return print_social
    final_data = data.split()
    j = 0
    while j<=(len(final_data)-2):
        if final_data[j] not in print_social:
            print_social[final_data[j]] = final_data[j+2].split(',')
        j = j+3
    return print_social

   
def main():
    '''
        handling testcase input and printing output
    '''
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'
    #print(string[0].split())
    print(create_social_network(string))

if __name__ == "__main__":
    main()
