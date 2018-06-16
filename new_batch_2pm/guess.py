import random

comGuess = random.randint(1,50)

count = 1

while True :

    userGuess = int(input("\nEnter your Guess - ").strip())
    count += 1

    if comGuess > userGuess :

        print("\nBe Big Think Big\n")

    elif comGuess < userGuess :

        print("\nBe in Limits Think Lower\n")

    else :

        print("\nYeah!! You have won The Game \n")
        break

    if count > 5 :
        
        print("\nYou are such a Looser\n")
        break


