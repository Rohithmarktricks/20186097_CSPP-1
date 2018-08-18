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

# def second_degree(a,b,c):
# 	def values(x,y):
# 		return a*x**2 + b*x*y + c*y**2
# 	return values

# fun = second_degree('a','b','c')
# fun2 = second_degree('x','y','z')
# print(fun(1,2))

# import string
# d = {}
# #s = string.ascii_lowercase[:]
# a = 'alkdfibaeuberkgbakfaerniorhwebfalwkfnaoieu'
# for i in a:
# 	if i not in d:
# 		d[i] = 1
# 	else:
# 		d[i] += 1

# l = list(set(d.values()))
# print(l)
# for i in l:
# 	if i not in new.keys():
# 		pass
#print('{} {} {}'.format(* 'abs'))

# stop = ['is', 'a', 'be']
# sentence = ['RaJu', 'is', 'a', 'be', 'random']
# for i in sentence:
# 	if i in stop:
# 		sentence.remove(i)
# print(sentence)

# from string import Template

# t = Template('Hi, I am $name\n')

# names = ['Rohith', 'Sam', 'Saiteja']
# for i in names:
# 	print(t.substitute(name = i))

# d = {1:"Rohith", 2:'Saiteja', 3:'Sam'}
# #print(d.values())
# print([i+'!' for i in d.values()])
# #print(x)
# a = [6, 7, 8, 9, 10]
# print(list(map((lambda x:x**2), a)))
'''
Example for functions for map in python
def squ(x):
	return x**x
def cub(x):
	return x*x*x

funcs = [squ, cub]

list_ = [1, 2, 3, 4]
for i in list_:
	print(map(lambda x:x(i), funcs))
'''
# a = [1, 2, 3, 4, 5, 6, 2]
# b = [5, 6, 7, 5, 2, 10, 2]
#print([str(x for x in a if x in b).strip()])

init_tuple = [(0, 1), (1, 2), (2, 3)]

result = sum(n for _, n in init_tuple)
print()
print(result)