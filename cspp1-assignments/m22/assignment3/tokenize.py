'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
adict = {}
def tokenize(string):
    for word in string:
    	if word not in adict:
    		adict[word] = 1
		else:
			adict[word] += 1
	return adict
            
def main():
	'''
	,Main function
	'''
	num = int(input())
	for i in num:
		new = tokenize(input())
	print(new)
if __name__ == '__main__':
    main()
