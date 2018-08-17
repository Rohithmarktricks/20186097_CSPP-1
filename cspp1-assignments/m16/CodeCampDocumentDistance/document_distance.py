'''
    Document Distance - A detailed description is given in the PDF
'''
import math
import re
# new = re.sub('[^A-Za-z0-9]+', ' ', exp)
# print(new)

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dict1 = dict1.lower().strip()
    dict2 = dict2.lower().strip()
    dict1 = re.sub('[^A-Za-z]+', ' ', dict1)
    dict2 = re.sub('[^A-Za-z]+', ' ', dict2)
    word1 = dict1.split()
    word2 = dict2.split()
    # word1 = word1.strip()
    # word2 = word2.strip()
    for i in word1:
        if i in '0123456789':
            del i
    for j in word2:
        if j in '0123456789':
            del j
    file_stop = load_stopwords("stopwords.txt")
    for h in file_stop:
        if h in word1:
            word1.remove(h)
    file_stop = load_stopwords("stopwords.txt")
    for k in file_stop:
        if k in word2:
            word2.remove(k)
    final_dict = {}
    final_dict2 = {}
    final_list = []
    for l in word1:
        final_dict[l] = final_dict.get(l, 0)+1         
    for m in word2:
        final_dict2[m] = final_dict2.get(m, 0)+1
    new_dict = {}
    new_common_keys = list(set(final_dict.keys()) & set(final_dict2.keys()))
    for i in new_common_keys:
        new_dict[i] = [final_dict[i], final_dict2[i]]
    for i in final_dict:
        if i not in new_dict:
            new_dict[i] = [final_dict[i], 0]
    for i in final_dict2:
        if i not in new_dict:
            new_dict[i] = [0, final_dict2[i]]


    numer = sum(new_dict[i][0]* new_dict[i][1] for i in new_dict)
    denomi = math.sqrt(sum(new_dict[i][0]**2 for i in new_dict)) * math.sqrt(sum(new_dict[i][1]**2 for i in new_dict)) 
    return round(numer/denomi, 2)





def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()
    # input1 = load_stopwords(input1)
    # input2 = load_stopwords(input2)

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
