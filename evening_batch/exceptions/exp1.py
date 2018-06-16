while True:
    try :
        var = int(input("Enter an intiger - ").strip())
        break
    except:
        print("Error!!! only int please ")
print("You have sucessfully entered an integer ",var)
