N = int(input("Enter the number	:"))
if N < 0 :
	N = abs(N)
for i in range(-N,N+1,1):
	print(i)
