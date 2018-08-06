import requests
import json

#url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=26.922070,75.778885&radius=5000&types=food&name=burger&key=AIzaSyBDB7zeAt8y9d9fykfW3SzPaT2EQUEYl8s"

url = "https://maps.googleapis.com/maps/api/place/autocomplete/json?input="

url2 = "&types=geocode&key=AIzaSyBy6pJs4DApRua7iNF0T4DNSksHLoshyf8"
url1 = input("Enter location to know abour place - ")
url = url+url1+url2
data = requests.get(url)




k = data.json()

place_id = k['predictions'][0]['place_id']

n_url = "https://maps.googleapis.com/maps/api/place/details/json?placeid="+place_id+"&key=AIzaSyBy6pJs4DApRua7iNF0T4DNSksHLoshyf8"

d1 = requests.get(n_url)

d2 = d1.json()

print("Info about - ",url1)
print("Address = ",d2['result']["formatted_address"])
print("lat = ",d2['result']['geometry']['location']['lat'])
print("lng = ",d2['result']['geometry']['location']['lng'])
