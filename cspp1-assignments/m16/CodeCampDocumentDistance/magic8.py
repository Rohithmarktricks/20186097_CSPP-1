import random
answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
print("Hello, I am magic8game. I may help you to make decisions")
name = input("Enter your name	:")
print('Hello'+name)

def magic8game():
	question = input("Ask me a question?")
	print("Thinking.....")

	print(random.choice(answers))
	print('I hope that helped!')
	#replay()

# def replay():
# 	print("Do you want to ask again or quit the game?")
# 	input2 = input("Enter 'Y' to ask or 'N' to quit")
# 	if input2 == 'Y':
# 		magic8game()
# 	elif input2 == 'N':
# 		exit()
# 	else:
# 		print("Apologies I did not catch that. Please repeat")
# 		replay()

# magic8game()
while True:
	question()
    repeat = input("Would you like to ask another question? (Y or N)")
    if not (repeat == "y" or repeat == "Y"):
        print("Come back if you have more questions!")
        break