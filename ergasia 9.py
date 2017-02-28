import requests
import json

src = raw_input('dwse anazhthsh')
keywords = [x.strip() for x in src]
beers=[]
def save(key):
    parameters = { "q": key, "type": "beer", "key": "44e261b18f373f3ae07b271ea7be8ca3", "format": "json"}
    response = requests.get("http://api.brewerydb.com/v2/search",params=parameters)
    data = response.json()
    beers.append(data)
    return data

key = src
key in keywords
data = save(key)
delimiter = ','
search = src.split(delimiter)
lng = len(search)
maxid = "none"
maks = -1
for i in range(49):
    a = (data["data"][i]["description"])
    count = 0
    for p in range(lng):
        count = count + a.count(search[p])
    if (maks<count):
        maks = count
        maxid = (data["data"][i]["id"])
print maks , maxid
