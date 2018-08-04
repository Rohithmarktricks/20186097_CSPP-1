num = float(input("Enter the number	:"))
init = 0.0
last = num
elipson = 0.001
num_guesses = 0
guess = (init + last)/2
while abs(guess**2 - num) >= elipson:
	if guess**2 < num:
		init = guess
	else:
		last = guess
	guess = (last + low)/2.0
num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', num)
