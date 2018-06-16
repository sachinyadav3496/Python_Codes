def myerror():
    try :
        a = int(input("please enter a value (positive) - "))
        assert ( a > 0 ), "Got you ,are you over smart,\n type in as i say to you "
    except AssertionError as a:
        print("Error!!!!",a)
        myerror()
    else:
        print("you are a good booooy")

if __name__ == "__main__" :
    print("Program begins here \n\n\n")
    myerror()
    print("\n\nProgram ends here")

