class Bag:
    def __init__(self):
        self.data = []
    def add(self,x):
        self.data.append(x)
    def addtwice(self,x):
        self.add(x)
        self.add(x)
obj1 = Bag()
obj1.add(1)
obj1.add(2)
print(obj1.data)
obj1.addtwice(3)
print(obj1.data)
