def fact(num):

    if num == 1 :

        return 1

    else :

        return num*fact(num-1)


print("Result = %s"%fact(int(input("Enter a no. - "))))

