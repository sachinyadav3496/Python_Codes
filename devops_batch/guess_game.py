from random import randint
import os
os.system('cls')
print("\n\n\n\n")
while input("Do you wanna play... than press any key ") :
    os.system('cls')
    print("\n\n\n")
    comGuess = randint(1,50)
    for var in range(1,6):
        userGuess = int(input("Your Guess (1,50) : ")) 
        if userGuess > comGuess :
           print("Think Lower Be in Limits")
        elif userGuess < comGuess : 
            print("Be Big Think Big")
        else :
            print("You Have Won This Game ")
            input()
            break
        if var == 5 : 
            print("You Such a Looser")
            print("Computer Guess was :  ",comGuess)
            input()
    os.system('cls')
    print("\n\n\n\n")
os.system('cls')
