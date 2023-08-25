#x=[22,45,99,65,78]
#x.sort()
#print(max(x))

##################################################################33333

import requests

url=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

print(url.json()['bpi']['USD'])
