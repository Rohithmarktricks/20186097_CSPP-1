str1 = 'abcdefghijk'
letters_available = 'abcdefghijklmnopqrstuvwxyz'
for i in str1:
	if i in letters_available:
		new_str = letters_available.replace(i,'')
print(new_str)

list1 = ['a','e']
for j in list1:
	print(j)