__author__ = 'Sachin Yadav'
import json
f = open('test1.txt','w+')
user = { 'name':['ram','shyam','mohan'],'acc':[1001,1002,1003,1004],'bal':[0,0,0]}
k=str(user)
f.write(k+'\n')
f.seek(0)
s =  f.read()
print(s)
list = [1,2,3,4,5,6]
l = str(list)
f.write(l+'\n')
f.seek(0)
s=f.read()
print(s)
f.seek(0)
temp=f.readline()
d = json.loads(temp)
print(d)

f.close()