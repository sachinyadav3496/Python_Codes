def reverse(n):
    """ reverse(n)-> takes an argument n and return it's reverse no. """
    r = 0   
    while n > 0:
        t = n % 10 
        r = r*10 + t
        n //= 10
    return r

def main():
    """main()-> A function to check palindrome no. """
    n = int(input("\nEnter a no. "))
    print()
    r = reverse(n)
    print("Reverse of ",n," is = ", r)
    print()
    if n == r :
        print(n,"is Palindrome")
    else:
        print(n,"is not a palindrome")

if __name__ == "__main__" :
    print("-----------------------------------------------------------------")
    print()
    while True:
        main()
        ch = input("\nDo you want to continue y/n - ")
        if ch.lower() == 'y' :
            pass #continue
        elif ch.lower() == 'n':
            break
        else:
            print("Wrong Choice i/p - ")
            ch = input("Enter your choice - ")

    print()
    print("-----------------------------------------------------------------")
