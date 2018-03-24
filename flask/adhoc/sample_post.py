import requests
import rssi
import json
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
data=rssi.d
r=requests.post("http://localhost:5000/hi",data=json.dumps(data),headers=headers)

print r.text

