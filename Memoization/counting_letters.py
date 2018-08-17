final_dict = {}
#str_ = input("Enter the string	:")
str_ = "to be or not be - A".split(" ")
for i in str_:
	final_dict[i] = final_dict.get(i, 0)+1			
print(final_dict)