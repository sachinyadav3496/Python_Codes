def anything():
    try : 
        x = int(input("Enter x : "))
        y = int(input("Enter y : "))
        r = x / y 
        print("Division of {x} and {y} is {r} ".format(x=x,y=y,r=r))
    except ValueError as e : 
        print("Please input only integer ")
        anything()
    except ZeroDivisionError as e : 
        print("Please Do not Divide by Zero")
        anything()
    except KeyboardInterrupt as e:
        print("Please complete the program ")
        anything()
    except Exception as e : 
        print("Error!!",e)
        anything()
    else : 
        print("Well Done")
    finally : 
        print("I will print Always ")

anything()


