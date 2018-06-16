n = int(input("Enter a no - "))

s = str(n)
t = s[::-1]
N = int(t)

print("Reverse of no. ",n, " is = ", N)

if n == N :
    print("No. is palindrome ",n)
else :
   print("No. is not palindrome ",n)
