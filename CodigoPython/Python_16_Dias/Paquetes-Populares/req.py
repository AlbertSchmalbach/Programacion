import requests

# get

url = "https://jsonplaceholder.typicode.com/users"

# r = requests.get(url, timeout=10)

# # print(r.status_code)
# # print(r.text)

# r = r.json()

# for user in r:
#     print(user["name"])

# post



# user = {
#     "id":11,
#     "name": "Misuri Atencia"
# }

# r = requests.post(url, timeout=10, data=user)
# print(r.status_code)

apikey= "12345"
headers = {
    "Authorization": f"Bearer {apikey}"
}
r = requests.post(url, timeout=10, headers=headers)
print(r.status_code)