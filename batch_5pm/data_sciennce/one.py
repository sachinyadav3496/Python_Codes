from math import log10
from random import randint
from time import sleep

N = int(input("Enter number of observations : "))
s,e = list(map(int,input("Enter Range(s-e) : ").split('-')))
print("\nCreating data sets")
sleep(2)

data = [ randint(s,e) for var in range(N) ]

print(*data)


k = round(1+3.322*log10(N))
c = (e-s) / k 
print("Number of Class-intervals = ",k)
print("Width of each classs = ",f'{c:.2f}')

x = [] 
s = float(s)
for var in range(k) : 
    x.append((s,s+c))
    s = s+c

#print("Class Intervals are --> ")
#print('\nClass')
#for var in x : 
#   print(var[0],var[1],sep='-')

f = [] 

u_data = set(data)

for var in x:
    s,e = var
    cf = 0
    for item in u_data :

        if item >= s and item < e : 

            cf = cf + 1
    f.append(cf)

#print("Frequency table = ",*f)


new_data = list(zip(x,f))

print("\t\t\tClass\t\tFrequency")
print("\t\t",'-'*40)
for x,f in new_data : 
    
    print("\t\t|\t",end='')
    print(f'{x[0]:.2f}',f'{x[1]:.2f}',sep=' - ',end='\t')
    print("|",end='')
    d = str(f)+'\t|'
    print(d.rjust(12))
print("\t\t",'-'*40)