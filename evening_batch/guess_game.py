import random
ComGuess = random.randint(0,101)

while True:
    UserGuess = int(input("Enter your Guess - "))
    if UserGuess > ComGuess :
        print("Be in Limits - Think Lower ")
    elif UserGuess < ComGuess :
        print("Be Big  - Think Big ")
    else :
        print("Yeah!!! You have won the game ")
        break
