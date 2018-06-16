def info(name, *var):
    "this is something cool"
    print("The given info is as - ")
    print(name)
    for i in var:
        print(i)
    print("Now we access args with index values")
    print("name ",name,"index[0]",var[0],"index[1]",var[1])
    return 
info("sachin",10,20,"babu","sona","mona")


