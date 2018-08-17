# exp = "A string is - there ? \n"
# print(exp.lower().strip())

# #[^A-Za-z0-9]+
# exp = "hello 123"
# import re
# new = re.sub('[^A-Za-z]+', ' ', exp)
# print(new)


# d = {}
# d1 = {"a":1, "b":2, "cc":3}
# d2 = {"aa":1, "b":3, "c":3}
# hi = list(set(d1.keys()) & set(d2.keys()))
# for i in hi:
# 	d[i] = [d1[i], d2[i]]
# print(d)

'''
function calling another fuction
'''
# def g():
# 	print("Hi, It's me 'g'")
# 	print("Thanks for calling me!")
# def f(func):
# 	print("I am 'f'")
# 	print("Now I would like to intoduce another function")
# 	func()
# 	print("The funcs true name is", func.__name__).

# f(g)

'''
Function that returns another function!
'''
# To calculate a.x^2 + b.x.y + c.y^2

def second_degree(a,b,c):
	def values(x,y)