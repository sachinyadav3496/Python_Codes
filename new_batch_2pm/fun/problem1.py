n = int(input())
print(*list(map(lambda x:True if int(x) % 2 == 0 else False,input().split())))
