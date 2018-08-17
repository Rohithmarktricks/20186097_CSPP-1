'''
    Document Distance - A detailed description is given in the PDF
    @author : Rohithmarktricks
'''
import math
import re
SPECIAL_CHARS = ',./?!@#$%^&*()_:;[]+*-/~`'

def create_dict(final_dict, final_dict2):
    '''
    Takes two dictionaries and returns a single dictionary
    that has the frequency of words.
    '''
    new_dict = {}
    new_common_keys = list(set(final_dict.keys()) & set(final_dict2.keys()))

    for i in new_common_keys:
        if i not in new_dict:
            if i not in SPECIAL_CHARS:
                if len(i) > 0:
                    new_dict[i] = [final_dict[i], final_dict2[i]]
    for i in final_dict:
        if i not in new_dict:
            if i not in SPECIAL_CHARS:
                if len(i) > 0:
                    new_dict[i] = [final_dict[i], 0]
    for i in final_dict2:
        if i not in new_dict:
            if i not in SPECIAL_CHARS:
                new_dict[i] = [0, final_dict2[i]]
    return final_cal(new_dict)

def final_cal(new_dict):
    '''
    This finally calcualtes the score
    '''
    numer = sum(new_dict[i][0]* new_dict[i][1] for i in new_dict)
    denomi = math.sqrt(sum(new_dict[i][0]**2 for i in new_dict)) \
    * math.sqrt(sum(new_dict[i][1]**2 for i in new_dict))
    return round(numer/denomi, 1)

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename1:
        for line in filename1:
            stopwords[line.strip()] = 0
    return stopwords

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dict1 = re.sub('[^A-Za-z]+', ' ', dict1).lower().strip().split()
    dict2 = re.sub('[^A-Za-z]+', ' ', dict2).lower().strip().split()

    # Load stopwords here.
    file_stop = load_stopwords("stopwords.txt")

    final_dict = {}
    final_dict2 = {}
    for l_iter in dict1:
        if l_iter not in file_stop:
            if len(l_iter) > 0:
                final_dict[l_iter] = final_dict.get(l_iter, 0)+1
    for m_iter in dict2:
        if m_iter not in file_stop:
            if len(m_iter) > 0:
                final_dict2[m_iter] = final_dict2.get(m_iter, 0)+1
    return create_dict(final_dict, final_dict2)


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
