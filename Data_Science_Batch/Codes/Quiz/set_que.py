import json
def entry(data):
        q = input("Enter Question : \n")
        op = input("Options as A,B,C,D : ").split(',')
        ans = input("Ans - ")
        n = [q,op,ans]
        data.append(n)
        f = open('nqdata.txt','w')
        json.dump(data,f)
        f.close()
        if input("Press a key : ") :
            entry(data)
def main():
    try :

        f = open('nqdata.txt')
        data = json.load(f)
        f.close()
        entry(data)
    except Exception as e :
        f = open('nqdata.txt','w')
        data = [] 
        entry(data)

if __name__ == "__main__" :
    main()
