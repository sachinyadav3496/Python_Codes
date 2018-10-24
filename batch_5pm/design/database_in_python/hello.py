name = input("Enter your name : ")
print(f"welcome mr {name} to the Design and Development Part")

data = { 'name' : name,
        'age' : input("Enter your age : "),
        'country' : input("Enter your country : "),
        'type' : None,
        'Programmer' : True,
        'good at something' : False,
        'skills' : [ 'c','c++','java','python' ]
        }

import json
f = open('data.db','w')

json.dump(data,f)


f.close()
