'''
    This is a continuation of the social network problem
    There are 3 functions below that have to be completed
    Note: PyLint score need not be 10/10 for this assignment. We expect 9.5/10
'''
# PRINT_SOCIAL = {}
# LINES = 0
# def create_social_network(data):
#     # return PRINT_SOCIAL
#     final_data = data.split()
#     j = 0
#     while j <= (len(final_data)-2):
#         if final_data[j] not in PRINT_SOCIAL:
#             if final_data[j+1] == 'follows':
#                 PRINT_SOCIAL[final_data[j]] = final_data[j+2].split(',')
#         j = j+3
#     return PRINT_SOCIAL
def follow(adict, arg1, arg2):
    '''
        3 arguments are passed to this function
        network is a dictionary representing the social network
        arg1 and arg2 are two people in the network
        follow function is called when arg1 wants to follows arg2
        so, this should result in adding arg2 to the followers list of arg1
        update the network dictionary and return it
    '''
    # print(network.keys())
    # print(arg1 in network.keys())
    # print(network[arg1])
    #L = network
    # for i in adict:
    #     if str_ in adict[i]:
    #         L.append(i)
    # return 
    for i in list(adict):
        # print(i)
        # print(arg1)
        if i == arg1:
            #print(adict[i])
            #print(adict[i])
            adict[i].append(arg2)
            #print(adict)
        if arg1 not in list(adict):
            adict[arg1] = arg2

    return adict
    
def unfollow(adict, arg1, arg2):
    '''
        3 arguments are passed to this function
        network is a dictionary representing the social network
        arg1 and arg2 are two people in the network
        unfollow function is called when arg1 wants to stop following arg2
        so, this should result in removing arg2 from the followers list of arg1
        update the network dictionary and return it
    '''
    for i in list(adict):
        # print(i)
        # print(arg1)
        if i == arg1:
            j = index(arg2)
            #print(adict[i])
            del adict[i][j]
            #print(adict)
    return adict
    


def delete_person(adict, arg1):
    '''
        2 arguments are passed to this function
        network is a dictionary representing the social network
        arg1 is a person in the network
        delete_person function is called when arg1 wants to exit from the network
        so, this should result in deleting arg1 from network
        also, before deleting arg1, remove arg1 from the everyone's followers list
        update the network dictionary and return it
    '''
    #print(adict.keys())
    for i in list(adict):
        if arg1 in adict[i]:
            adict = adict[i].remove(arg1)

        if arg1 in list(adict):
            del adict[arg1]
    return adict

def main():
    '''
        handling testcase input and printing output
    '''
    network = eval(input())
    lines = int(input())
    for i in range(lines):
        i += 1
        line = input()
        output = line.split()
        #print(output)
        if output[0] == "follow":
            network = follow(network, output[1], output[2])
            #print(network)
        elif output[0] == "unfollow":
            network = unfollow(network, output[1], output[2])
            print(network)
        elif output[0] == "delete":
            network = delete_person(network, output[1])

    print(network)

if __name__ == "__main__":
    main()
