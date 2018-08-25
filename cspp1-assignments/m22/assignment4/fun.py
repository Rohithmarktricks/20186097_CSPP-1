new = {'lorem': 1, 'ipsum': 2, 'porem': 2}
key = []
value = []
for keys in new.items():
	key.append(keys)
key.sort()
print(key)
for i in range(len(key)):
	print(str(key[i][0])+' - '+str(key[i][1]))
# for k in key:
# 	val = new[key]
	
