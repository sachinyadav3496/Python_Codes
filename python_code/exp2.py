try:
    f = open("hey",'r')
    f.write("All is Well")
except:
    print("Some kind of error!")
else:
    print("Content Written successfully")

