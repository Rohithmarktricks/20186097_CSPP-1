s = [[1,2,3],[4,5,6],[7,8,9]]
# print(zip(*s))
#for y in zip(*s):
#   print(y)
# a = [1,2,3]
# b = [4,5,6]
# for i in zip(a,b):
#   print(i)
# a = [[1,2,2],[2,2,3]]
# new = 0
# for row in a:
#   new += row.count(2)
# print(new)
# dict_ = {'a':1, 'b':2, 'c':3}
# print(zip(*dict_))
# for i, j in dict_.items():
#   print(i,j)
#sample =

def transpose(s):
    new = []
    new2 = []
    k = 0
    def real_transpose(s):
        nonlocal new
        nonlocal new2
        nonlocal k
        if k < 3:
            for i,j in enumerate(s):
                new.append(j[k])
                break
            new2.append(new)
            k += 1
            real_transpose(s)
    print(new2)
    



#new2.append(new)
    # for k,l in enumerate(j):
    #   print(k,l)
# rows = len(s)
# columns = len(s[0])
# final_transpose = []
# for i in range(rows):
#       for j in range(columns):
#         if i == j:
#             final_transpose[i][j] = s[i][j]
#         else:
#             final_transpose[i][j] = s[j][i]
#   print(final_transpose)