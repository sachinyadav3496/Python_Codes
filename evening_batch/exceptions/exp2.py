while True:
    try :
        a = int(input(" a = ").strip())
        b = int(input(" b = ").strip())
        result = a/b
        break
    except Exception as e:
        print("Error!!!",e)
print(str(a)+"/"+str(b)+"="+str(result))
