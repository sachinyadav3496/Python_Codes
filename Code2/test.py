import time
t = time.time()
for var in range(5):
    for j in range(var):
        print("*",end='')
        time.sleep(.2)
    print()
print("\n\nYour execution time is - ",time.time()-t)
