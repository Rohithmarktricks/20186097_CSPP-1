final_dict = {}
str_ = input("Enter the string	:")
for i in str_:
	final_dict[i] = final_dict.get(i, 0)+1			
print(final_dict)