from sys import argv
script,input_file = argv
def print_all(f):
    print(f.read())
def rewind(f):
    f.seek(0)
def print_a_line(line_count,f):
    print(line_count+1,f.readline())
current_file = open(input_file)
print("Let's print the whole file \n")
print_all(current_file)
print("Now let's Rewind, kind of like tape")
rewind(current_file)
print("Let's print 3 lines - ")
for line in range(0,5):
    print_a_line(line,current_file)

    
