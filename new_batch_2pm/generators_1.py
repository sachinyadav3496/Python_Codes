def Reverse(data):

    for index in range(len(data)-1,-1,-1) : 

        yield data[index]

def Main():
    rev = Reverse(input("Type to reverse : "))
    for ch in rev : 
        print(ch)

Main()

