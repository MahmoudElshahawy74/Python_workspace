
import requests

activity=requests.get("https://www.boredapi.com/api/activity")

cur_activity=activity.json()["activity"]


print(cur_activity)
