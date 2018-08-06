import os
def read():
    filename = input("Enter Absolute path to open a file : ")
    try :
        f = open(filename)
        data = f.read()
        f.close()
        print("\n\n\n")
        print(data)
    except Exception as e :
        print("Error!",e)

def write(fname):
    try :
        f = open(fname,'w')
        print("use :wq to save file")
        print("\n\n\n")
        while True:
            data = input()
            if data.lower() == ':wq' :
                f.close()
                break
            else :
                f.write(data)
                f.write('\n')
            
    except Exception as e :
        print("Error! ",e)

def new_file():
    filename = input("Enter file name with path : ")
    try :
        if os.access(filename,os.F_OK) :
            print("File already Exists")
            print("Do want to overwrite File ")
            ch = input("y/n : ").strip().lower()
            if ch == 'y' :
                write(filename)
        else :
            write(filename)
    except Exception as e :
        print("Error!!",e)
def append():
    filename = input("Enter file name with path : ")
    if os.access(filename,os.F_OK):
        try :
            f = open(filename,'a+')
            f.seek(0)
            d = f.read()
            print(":wq to exit text editor")
            print("\n\nDATA\n\n")
            print(d)
            while True :
                data = input()
                if data.lower() == ':wq' :
                    f.close()
                    break
                else :
                    f.write(data)
                    f.write('\n')
        except Exception as e :
            print("Error!",e)
    else :
        print("\n\nNo such file exists")
        print("Try Again")
def rename():
    filename = input("Enter file name with path : ")
    if os.access(filename,os.F_OK):
        new_name = input("New name :")
        k = filename.split('/')
        k.pop()
        k.append(new_name)
        n = '/'.join(k)
        os.rename(filename,n)
    else :
        print("Error!!No such file Exists")
def delete():
    fname = input("Enter path : ")
    if os.access(fname,os.F_OK) :
        os.unlink(fname)
    else :
        print("No such file Exists")
    
def menu():
    print("1.Open\n2.New File\n3.Append\n4.Rename\n5.Delete\n6.Exit")
    ch = int(input("Choice : ").strip())
    if ch == 1 :
        read()
    elif ch == 2 : 
        new_file()
    elif ch == 3 :
        append()
    elif ch == 4 :
        rename()
    elif ch == 5 :
        delete()
    elif ch == 6 :
        exit(0)
    else :
        print("Invalid Choice ")
    
    menu()
if __name__ == "__main__" :
    menu()
