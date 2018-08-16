def fib_memo(n, d):
	if n in d:
		return d[n]
	else:
		ans = fib_memo(n-1, d) + fib_memo(n-2, d)
		d[n] = ans
		return ans

d = {1:1, 2:1, 3:2}

int_int = int(input("Enter the number"))
print(fib_memo(int_int, d))