def take_input():

    try : 
        k = int(input("Enter a int no - "))
        return k 

    except Exception as e : 
        print("Error!!",e)
        print("Please Input only an integer no. - ")
        return  take_input()

var = take_input()
print(var)
