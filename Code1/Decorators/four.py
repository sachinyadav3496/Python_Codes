def g():
    print("Hi,it's me 'g'")
    print("Thanks for calling me")
def f(func):
    print("Hi,it's me 'f'")
    print("I will call 'func' now")
    func()
f(g)
