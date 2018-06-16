def myFun(arg1,arg2='python',*args,**kwargs):

    """myFun(arg1,[,arg2='python',*args,**kwargs])->This function takes one positional argument and 3 optional arguments.\
\n It is to understand arguments and string formating.\
\nIt will print out all the arguements with keys and \
return a string 'Programs ends here'. """
    
    print("Positional Argument arg1 = %s"%(arg1))

    print("Default Argument arg2 = %s"%(arg2))

    count = 1

    for value in args:

        print("Multiple Argument args%i = %s "%(count,value))

        count += 1

    for key in kwargs :

        print("Multiple Argument Kwargs %s = %s "%(key,kwargs[key]))

    return "Function Ends Here "

print("\n\nDefination of myFun = %s"%(myFun.__doc__))

print("\n\nCalling myFun('arpit')")
print(myFun('arpit'))

print("\n\nCalliing myFun('arpit','JAVA',)")

print(myFun('arpit','JAVA'))

print("\n\nCalling myFun('sachin','Aditi','tuple','Grras','Arpit','Whatever')")

print(myFun('sachin','Aditi','tuple','Grras','Arpit','Whatever'))


print("\n\nCalling myFun('sachin','aditi','tuple','Grras','Rajat',name='arpit',age='30',sal=0,pos='Useless')")

print(myFun('sachin','aditi','tuple','Grras','Rajat',name='arpit',age='30',sal=0,pos='Useless'))
