
fp = open("C:\\Users\\sachin yadav\\Desktop\\helo.txt","r+")

data = fp.read()

print("hello file before changing")
print(data)

print("file is open to write")
print("press :wq to exit")

while True:
    
    s = input()
    if s == ":wq" :
        break
    else :
        fp.write(s)
        fp.write("\n")
  
fp.seek(0)

data = fp.read()

print("\n\nHere is your file ")

print(data)

print("We are exiting the program")
