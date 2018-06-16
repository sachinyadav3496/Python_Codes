import random

comGuess = random.randint(1,100)

c = 1

while c:

    userGuess = int(input("Enter Your Guess - "))

    if comGuess < userGuess :

        print("Think Lower Be in your limits ")

    elif comGuess > userGuess :

        print("Be Big Think Big ")

    else:

        print("Yeah!!You have won the game")
        break
    
    if c == 5 :

        print("You such a looser")
        c = 0

    else:

        c += 1
    


