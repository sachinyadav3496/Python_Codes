f = open('data.db')


import json

data = json.load(f)

f.close()

print(data)


while input("Press any key to continue operations : ") : 


    key = input("Enter any key you want to lookup : ")

    info = data.get(key,'Value not Found')

    print("Here is the answere of your query ")

    print(f"{key} = {info} ")

