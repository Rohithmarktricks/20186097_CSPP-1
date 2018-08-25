'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''
KEY = []
def frequency_graph(dictionary):
	'''
	Frequency_graph function!
	'''
    for keys in dictionary.items():

        KEY.append(keys)
    KEY.sort()
    for i in range(len(KEY)):
        print(str(KEY[i][0])+\
        	' - '+'#'*KEY[i][1])



def main():
	'''
	Main function
	'''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
