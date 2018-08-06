import urllib.request
import urllib.parse

try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    print(x.read())

except Exception as e:
    print(str(e))

try:
    url = 'https://www.google.com/search?q=test'

    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (x11; Linux i686) AppleWebKit/537. '

    req = urllib.request.Request(url,headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('withHeaders.txt','w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print(str(e))
