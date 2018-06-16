print("Enter Path to create new file")

path = input("Path : ")

fp = open(path,'w+')

print("Enter Data to write into file\n")
c = 1
print("Write :w to save file")
while True:
    print("Write line%s: "%c,end='')
    s = input()
    if s.lower() == ':w' :
        break
    fp.write(s)
    fp.write("\n")

print("\nOptions\n1.Show Content\n2.Save and close")
ch = int(input("\nYour Choice : "))
if ch == 1 :
    fp.seek(0)
    print(fp.read())
    fp.close()
elif ch == 2 :
    fp.close()
    
print("File Saved SucessFully")

    
    
