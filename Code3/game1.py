import random
def game():
	comGuess = random.randint(1,100)
	while True:
		userGuess = int(input("Guess - "))
		if userGuess > comGuess :
			print("Be in limit - Think lower ")
		elif userGuess < comGuess :
			print("Be Big - Think Big ")
		else :
			print("Yeah! You have won ")
			break
game()
