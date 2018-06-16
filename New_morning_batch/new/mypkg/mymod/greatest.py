"""This contains a function call great and used calcultate greatest no. """

def great(x,y,z):

    """great(x,y,z)->take 3 positional arguments as x, y and z.
    will return greatest no among given three values x,y and z."""

    if x >= y and x >= z :

        return x

    elif y >= x and y >=z :

        return y

    else :

        return z



if __name__ == "__main__" :


    print("\n\nWelcome to Greatest no. program\n\n")

    x = int(input("Enter value of x = "))
    y = int(input("Enter value of y = "))
    z = int(input("Enter value of z = "))

    print("\n\n")
    
    res = great(x,y,z)
    print("Greatest num is - ",res)

    print("\n\nProgram ends here \n\n")


