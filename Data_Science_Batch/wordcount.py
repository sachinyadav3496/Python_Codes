import os

os.system('cls')

print("\n\n")
print("Welcome to WordCountProgram".center(230))

print("\n\n")
filename = input("Enter file Path : ") 
print("\n\n")

if os.path.exists(filename) : 
    if os.path.isfile(filename) : 
        if os.access(filename,os.R_OK) : 
            f = open(filename)
            data = f.read()
            f.close()
            lines = len(data.split('\n'))
            words = len(data.split())
            chars = 0 
            for char in data : 
                if char not in ( '',' ','\t','\n') : 
                    chars += 1
            print("\n\n")
            print(f"Number of lines {lines}")
            print(f"Number of words {words}")
            print(f"Number of Characters {chars}")

            print("\n\n")
            input("Press any key to exit ".rjust(25))





        else : 
            print("You Don't have Permission to Read This File")
    else : 
        print("You Idiot I asked for file not for Directory")
else : 
    print(f"Errorr!!Please Double Check Your Path Because These no such File Exists in your system with path {filename}")


print("\nThanks for using This Program")
os.system('cls')
