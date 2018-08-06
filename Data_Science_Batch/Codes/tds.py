from random import randint,choice
from time import sleep
from os import system


n = int(input("\n\n\n\n\t\tEnter number of players : "))
l = []
for var in range(n):
    system('cls')
    print('\n\n\n')
    l.append(input("\n\n\n\t\t\t\tName of Player[{}] : ".format(var+1)))
while input("\t\t\t\tPress any key to roll bottle : ") : 
    system('cls') 
    print("\n\n")
    print("\n\n\n\n\n")
    print("\t\t\t\tRolling....Rolling...\n\n")
    sleep(randint(1,5))
    print("\t\t\t\tTarget Player : {}".format(choice(l)))
    print("\n\n")
system('cls')
