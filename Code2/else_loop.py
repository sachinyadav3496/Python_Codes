
print()
print()


l = []

n = int(input("Enter no. of entries - "))

print()
print()


for var in range(n):
    
    s = "Enter value no. "+str(var)+" - "    
    
    l.append(input(s))


print("\n\nLoops Starts from here - \n\n")


for var in l:
    
    
    print("\n\n")
    print("Value of variable = ", var )
    
    
    if var == "exit" :
        break
    
    elif var == "skip" :
        continue
    
    
    print("Last statement of loop ")
    print("Loop Working fine")
    
    print()
    print()

else:
    print("NO break statement encounters ")


print("\n\nLoops end here\n\n")
