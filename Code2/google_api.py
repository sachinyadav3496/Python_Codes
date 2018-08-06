import requests
import json

#url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=26.922070,75.778885&radius=5000&types=food&name=burger&key=AIzaSyBDB7zeAt8y9d9fykfW3SzPaT2EQUEYl8s"

url = "https://maps.googleapis.com/maps/api/place/autocomplete/json?input="

url2 = "&types=geocode&key=AIzaSyBy6pJs4DApRua7iNF0T4DNSksHLoshyf8"
url1 = input("Enter location to know abour place ")
url = url+url1+url2
print(url)
"""
data = requests.get(url)



print(data.json())

k = data.json()

file = open("google_text",'w+')

json.dump(k,file)

file.close()



"""
