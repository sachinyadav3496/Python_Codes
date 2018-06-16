import requests
import time
import random
import json

token = "EAACEdEose0cBAAoiRuQKJCQ1NTF1yTieCrxZAFfLpsIB37reQJ8Pd7l6zfXpcHJMsCBe2u97N3aOVGCvg2xZC9vtkzjHBrShsnGCvtoAnXD5cZA6tNEa3GIeCIsOKWpGsjr9O2MAZCSZCcGXCh5T2hyITo47ZBmpqFhaIrwQU2fjlOJXIoNHbn8MPgIeWjvXLp4XKKXFYsmwZDZD"


#req = 'Steam?fields=posts.limit(50){message}' 


req = 'me?fields=id,name,posts'



def req_facebook(req):
    
    #print("https://graph.facebook.com/v2.10/"+req,{'access_token' : token})
    
    r = requests.get("https://graph.facebook.com/v2.10/"+req,{'access_token' : token})

    return r

results = req_facebook(req).json()

results = results['posts']['data']

for var in results:
    print("\n\n\n")
    print(var[1]['message'])


"""

print("\n\n\nHere is your data - \n\n\n")

for keys in results:
    
    print("\n\n")
    
    print(results[keys])
    
    
    print("\n\n")
f = open('myfacebook','w')

json.dump(results,f)

f.close() """
