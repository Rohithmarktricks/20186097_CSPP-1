def genFib():
	fib_1 = 0
	fib_2 = 1
	while True:
		next_ = fib_1 + fib_2
		yield next_
		fib_1 = fib_2
		fib_2 = next_

gen = genFib()

for i in range(10):
	del i
	print(gen.__next__(), end = ", ")
# print(gen.__next__())
print("")

