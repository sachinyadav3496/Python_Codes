# the following variable would be set as the result of a runtime calculation:
x = input("Do you need the answer? (y/n): ")
if x=="y":
    required = True
else:
    required = False
    
    
def the_answer(self, *args):              
        return 42
    
def augment_answer(cls):                      
    if required:
        cls.the_answer = the_answer
    # we have to return the class now:
    return cls
 
    
@augment_answer
class Philosopher1: 
    pass
@augment_answer
class Philosopher2: 
    pass
@augment_answer
class Philosopher3: 
    pass
 
    
plato = Philosopher1()
kant = Philosopher2()
  
    
# let's see what Plato and Kant have to say :-)
if required:
    print(kant.the_answer())
    print(plato.the_answer())
else:
    print("The silence of the philosphers")
