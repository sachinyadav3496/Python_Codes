

def myCalc(num1,num2,ch):

    if ch == '+' :

        return num1+num2
    
    elif ch == '-' :

        return num1-num2

    
    elif ch == '*' :

        return num1*num2

    elif ch == '/' :

        return num1/num2

    
    elif ch == '//' :

        return num1//num2

    elif ch == '**' :

        return num1**num2

    else :
        return "Error : Invalid Choice "

n = int(input("Enter no of items - "))

l1 = []
l2 = []
l3 = []

count = 1

for var in range(n) :

    l1.append(int(input("Enter data for list1 item no %s = "%(count))))
    l2.append(int(input("Enter data for list2 item no %s = "%(count))))
    l3.append(input("Enter Operation to perform +,-,*,/,//,** for set %s "%(count)))

    count += 1

res = []

for index in range(n):
    
    res.append(myCalc(l1[index],l2[index],l3[index]))

print(l1)
print(l2)
print(l3)
print(res)



