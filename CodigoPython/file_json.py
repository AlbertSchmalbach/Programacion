import json
from urllib import request

url = "https://my.api.mockaroo.com/personas.json?key=f39ea550"
res = request.urlopen(url)
# print(res.read())
data = res.read()
data = json.loads(data.decode('utf-8'))
print(data)