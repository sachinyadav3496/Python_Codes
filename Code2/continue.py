print()
print()
for i in range(51):
    print("\nValue of i = ", i , end = '' )
    if i % 5 == 0 :
        continue
    print("  Hello ! World ! \n")
print()
print()

k = 0

while k < 51 :
    k += 1
    if k % 5 == 0 or k % 2 == 0 :
        continue
    print("\nValue = ", k)
    
