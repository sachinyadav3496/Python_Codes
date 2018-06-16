import random

"""This module contain a function guess which is a guess game."""

def guessGame():

    """you have enter a randome choice b/w 1,50 if you guess correct then you will win else you \
            you have only 5 chances.

            """
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
            break
            

        else:

            c += 1
    

if __name__ == "__main__" :

    guessGame()
