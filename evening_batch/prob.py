l = []
n = int(input())

for _ in range(n):
    l.append([input(),float(input())])

l = sorted(l)
k = []
for name,marks in l:
    k.append(marks)

s = set(k)
s = sorted(s)

r = s[1]

for name,marks in l:
    if marks == r :
        print(name)
    else :
        pass


