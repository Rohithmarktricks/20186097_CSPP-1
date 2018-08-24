s = [[1,2,3],[4,5,6],[7,8,9]]
print(zip(*s))
#for y in zip(*s):
#	print(y)
# a = [1,2,3]
# b = [4,5,6]
# for i in zip(a,b):
# 	print(i)
a = [[1,2,2],[2,2,3]]
new = 0
for row in a:
	new += row.count(2)
print(new)