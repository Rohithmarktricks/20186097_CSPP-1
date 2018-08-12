# a = 'Rohith'
# b = ['Rohi','rohith','Rohith','Krishna']
# print(a in b)
count = 0
a = "Rohith"
print(a)
c = ['Rohith', 'rohith']
b = {'r':1, 'o':2, 'h':3, 'i':4, 't':5, 'h':6}
if a in c:
	for i in a:
		if i in b:
			count += 1		
print(count)
if count == len(a):
	print(True)
else:
	print(False)