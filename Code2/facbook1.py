import time
import requests
import time
import pickle
import random

token = 'EAACEdEose0cBAJNACDEEUotLbAulpiRcZAnANIpI1oKwjZAmqvGUIgsXVcu57Ww0jy0WyBDVWKpERYTx9SUMMP7FK6X7CHbSgzmG5JuvgDeWiaVZCKZC55XhNJaO7zts1pyuZBFmAtDYsdJTtbKtVd2ZAgHMKmvtBdU1UdijZAhqTm7YvpH2OTatpfy5za1exUZD'

#req = 'Steam?fields=posts.limit(50){message}' 
req = 'me?fields=id,name,posts'



def req_facebook(req):
    print("https://graph.facebook.com/v2.10/"+req,{'access_token' : token})
    r = requests.get("https://graph.facebook.com/v2.10/"+req,{'access_token' : token})

    return r

results = req_facebook(req).json()
print(results)
"""
data = []

#results = results['posts']
i = 0
while True:
    try :
        time.sleep(random.randint(2,5))
        data.extend(results['data'])
        r = requests.get(results['paging']['next'])
        results = r.json()
        i+=1

        if i > 10:
           break
    except :
        print("done")
        break

print(data)

#pickle.dump(data,open("steam_data.pkl","wb"))

#loaded_data = pickle.load(file=open("steam_data.pkl"))
"""
