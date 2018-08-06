d = { 'name' : 'hello' }
key = input("ente a key ")
try : 
    print(d[key])
except KeyError :
    print("NO such key exist in dictinory")
