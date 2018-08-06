import requests

url = input("Enter your url ")

fname = input("Enter your file with extention - ")

k = requests.get(url)

f = open(fname,'wb')

f.write(k.content)

f.close()

