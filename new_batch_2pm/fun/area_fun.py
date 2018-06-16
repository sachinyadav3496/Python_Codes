import math
def area(l,b=0,h=0):

    if b == 0 and h == 0 :

        ch = int(input("\nEnter your choice \n1.Squre\n2.Cube\n3.Circle\ninput = "))

        if ch == 1:

            return l*l
        
        elif ch == 2:

            return 6*l**2

        elif ch == 3 :

            return math.pi*l*l
       
        else :
            
            return 0

    elif h == 0 :

        ch = int(input("\nEnter your choice - 1.Rectangle\n2.Triange\ninput = "))

        if ch == 1 :

            return l*b

        elif ch == 2 :

            return 0.5*l*b

        else :

            return 0

    else:

        return 2*(l*b+b*h+h*l)



def main() :

    print("\n\nWelcome to Area Program \n\n ")
    print("1.Area of squre,cube,cirle")
    print("2.Reactangle or Triangle ")
    print("3.Cubiod")
    ch = int(input("Input = "))

    if ch == 1 :

        x = float(input("Enter side - "))
        result = area(x)
        print("\nArea = %.2f "%(result))

    elif ch == 2 :

        x = float(input("\nEnter side = "))
        y = float(input("\nEnter 2nd side = "))
        
        result = area(x,y)

        print("\nArea = ",result)

    elif ch == 3 :

        
        x = float(input("\nEnter side = "))
        y = float(input("\nEnter 2nd side = "))
        z = float(input("\nEnter 3rd side = "))

         
        result = area(x,y,z)

        print("\nArea = ",result)

    ch = input("\n\nDo you want to continue - y/n  ").strip()
    if ch.lower() == 'y' :

        main()
    

if __name__ == "__main__" :

    main()


