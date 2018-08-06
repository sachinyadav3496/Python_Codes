import sys

def add(a,b):
    return a+b

print("\n\nSystem Arguments = \n",sys.argv)

print("\n\nFile name = \n\n",sys.argv[0])
x = int(sys.argv[1])
y = int(sys.argv[2])

print("\n\nResult = \n\n",add(x,y))

