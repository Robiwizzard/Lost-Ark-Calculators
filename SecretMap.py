import http.client
import json

conn = http.client.HTTPSConnection("www.lostarkmarket.online")
conn.request("GET", "/api/export-market-live/Europe%20Central?category=Enhancement%20Material", '', {})
res = conn.getresponse()
data = res.read()
pricedata = json.loads(data)

def calc():

    for i in pricedata:
        if i["id"] == "solar-grace-1":
            sGrace = int(i["avgPrice"])
        if i["id"] == "solar-blessing-2":
            sBlessing = int(i["avgPrice"])
        if i["id"] == "solar-protection-3":
            sProtection = int(i["avgPrice"])
        if i["id"] == "honor-shard-pouch-l-3":
            pouch = int(i["avgPrice"])
    print("input price of level 4 gem:\n22.10.24: 465")
    lv4gem = int(input())
    print("input price of level 3 gem:\n22.10.24: 144")
    lv3gem = int(input())
    secretMap = 12*sGrace + 8*sBlessing + 4*sProtection + 8*pouch + lv4gem + lv3gem
    bid = (secretMap * 0.95 - (secretMap / 30)) / 1.1
    print("Secret map value: " + str(secretMap))
    print("Bid to maximize profit:" + str(int(bid)))

calc()