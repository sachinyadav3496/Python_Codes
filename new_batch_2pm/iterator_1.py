class myClass:
    def __init__(self,x):
        self.data = x
        self.index = len(x)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0 :
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

def main():

    obj = myClass(input("Enter string to reverse : "))
    while input("Press key to reverse : ") : 
        print(obj.__next__())


if __name__ == "__main__" :
    
    main()
