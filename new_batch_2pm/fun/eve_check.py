#k = input() #taking input as a list 

#k = k.split() #spliting string from spaces and storing it into a list 

#k = list(map(int,k)) #mapping all string integers from list to int fun and sotring it into list

#res = filter(lambda x:True if x % 2 == 0 else False , k)

#print(*res) #printing result as all even no

print(*list(filter(lambda x:True if x % 2 == 0 else False,map(int,input().split()))))
