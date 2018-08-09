def display(**kwargs):
	if kwargs is not None:
		for key,values in kwargs.items():
			#print("%s key has %s value" %(key,values))
			print("{} key has {} value".format(key,values))
			print(key,values)

sample_dict = {"1":"Rohith","2":"Computer Science","3":"Best"}
display(**sample_dict)