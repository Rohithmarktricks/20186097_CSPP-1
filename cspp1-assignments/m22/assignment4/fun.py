new = {'lorem': 1, 'ipsum': 2, 'porem': 2}
key = []
for keys in new.items():
	key.append(keys)
key.sort()
print(key)
for i in enumerate(key):
	print(i)
	print(str(key[i][1][0])+' - '+str(key[i][1][1]))

	
