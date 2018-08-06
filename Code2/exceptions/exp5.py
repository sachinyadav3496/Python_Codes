def err():
    try :
        f = open(input("Enter your path = "))
        print(f.read())
        f.close()
    except FileNotFoundError as e:
        print("Error!!!Mind your path because there is an error -\a ",e)
        err()
    finally :
        print("Main hoo Don!  Don! Don! ")
def main():
    print("\n\n\n\aProgram Ends Here")
    err()
    print("Program Begins here\n\n\n\a")

if __name__ == "__main__"  :
    main()
    
