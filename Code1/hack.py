from itertools import permutations as per
p,k=input().split()
l = list(per(sorted(p),int(k)))
for var in l:
    print((var[0]+var[1]).upper())
