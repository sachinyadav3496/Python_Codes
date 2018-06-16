while True:
    try :
        a = int(input(" a = ").strip())
        b = int(input(" b = ").strip())
        result = a/b
        break
    except ZeroDivisionError as e:
        print("Error!!! Hey are out of your mind \n Don't you know math \n nothing can be divided by zero ")
    except ValueError as e:
        print("Error!!! Think before you type \n I say only interger means only interger")
        
print(str(a)+"/"+str(b)+"="+str(result))
