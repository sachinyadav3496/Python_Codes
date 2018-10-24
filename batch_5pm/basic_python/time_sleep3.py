fp = open('output.txt','w')
for var in range(100):
    print("Hello World",file=fp)
fp.close()
