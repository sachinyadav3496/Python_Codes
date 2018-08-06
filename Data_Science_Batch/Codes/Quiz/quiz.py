import random
import json
import time

try :
    f = open('nqdata.txt')
    qlist = json.load(f)
    f.close()
except Exception as e :
    print("Something Went Wrong")
    print("Error:",e)

def paper():
    s = 0
    p = 2
    n = -1 
    random.shuffle(qlist)
    qno = 1
    for qs in qlist :
        print("\n\n\n")
        print("Q{}. {} ?".format(qno,qs[0]))
        random.shuffle(qs[1])
        print("\nA. {}\tB. {}\tC. {}\tD. {}".format(qs[1][0],qs[1][1],qs[1][2],qs[1][3]))
        print("\n\n")
        ch = input("Answer : ")
        i = qs[1].index(qs[2])
        if ch.lower() == 'a' :
            ans = 0
        elif ch.lower() == 'b' :
            ans = 1
        elif ch.lower() == 'c' :
            ans = 2
        elif ch.lower() == 'd' :
            ans = 3
        else :
            print("Invalid Choice")
            print("You loose this question Better luck next time")
            ans = 1000

        if i == ans : 
            s += p
        else :
            s += n
        qno = qno + 1
    return s

if __name__ == "__main__" :
    
    print("\n\nWelcome to Third Class Quiz \n\n")
    k = len(qlist)
    max_score = 2*k
    result = paper()
    print("Your score is = {} out of {}.".format(result,max_score))
    

