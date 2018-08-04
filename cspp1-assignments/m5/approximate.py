num = float(input("Enter the number   :"))
guess = 0.0
epsilon = 0.00000001
increment = 0.1
num_guesses = 0
while abs(guess**3 - num) >= epsilon and guess <= num:
  print(guess)
  guess += increment
  num_guesses +=1
print("No of num_guesses  :",num_guesses)

if abs(guess**3 - num) >= epsilon:
  print("Failed to find the cube .")
else:
  print("The cube of {} is {}".format(guess,num))

