n,k = map(int,input().split())

l = []
for var in range(n):

    l1 = list(map(int,input().split()))
    print(l1)
    t = max(l1)
    print(t)
    l.append(t)
s = 0 
for var in l:

    s+= pow(var,2)
    print("s = %d+%d"%(s,pow(var,2)))

res = s%k 
print(res)
