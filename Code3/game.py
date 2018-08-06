import random
comGuess = random.randint(1,100)
while True:
        userGuess = int (input("Guess - "))
        if userGuess > comGuess:
            print("Be in limit think lower ")
        elif userGuess < comGuess:
            print("Be Big - Think Big ")
        else:
            print("Yeah! you have won ")
            break
