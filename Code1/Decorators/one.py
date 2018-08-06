def succ(x): #defining Function
        return x+1
successor = succ #creating alice for function
print(id(succ)) #id will be same
print(id(successor)) #both of the function actually are one
print(successor(10)) 

del succ #deleting succ function more we can say removing alice succ
print(successor(10))  #it will still work
