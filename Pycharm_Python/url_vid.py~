import urllib.request as url
print("Welcome to BABA Downloader")
name = input("Enter file name with extention to save it ")
url_req = input("Enter your url to download - ")
file = url.urlopen(url_req).read()
f = open(name,'wb')
f.write(file)
f.close()


