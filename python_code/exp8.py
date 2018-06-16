n = int(input())
try:
    assert (n>0),"something went wrong"     
    print("every thing is fine",n)
except AssertionError as a:
    print("Enter valid input")
else:
    print("Sucesss")
