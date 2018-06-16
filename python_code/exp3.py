try:
    fh=open("kdg",'w')
    try:
        fh.write("something")
    finally:
        print("Going to close the file")
        fh.close()
except:
    print("I/O Error")
