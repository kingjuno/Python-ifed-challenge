# #1
# import requests

# url = "http://pokeapi.co/api/v2/pokemon/jigglypuff/"

# payload = ""
# response = requests.request("GET", url, data=payload)

# data = response.json()
# print("Type 1:",data["types"][0]["type"]["name"])
# print("Type 2:",data["types"][1]["type"]["name"])
import requests

url = "http://pokeapi.co/api/v2/pokemon/jigglypuff/"

url1=(data["types"][0]["type"]["url"])
url2=(data["types"][1]["type"]["url"])

payload1 = ""
payload2 = ""

response1 = requests.request("GET", url1, data=payload1)
response2 = requests.request("GET", url2, data=payload2)

data1 = response1.json()
data2 = response2.json()

for i in range(len(data1["damage_relations"]["double_damage_from"])):
  print(data1["damage_relations"]["double_damage_from"][i]["name"])
  
for i in range(len(data2["damage_relations"]["double_damage_from"])):
  print(data2["damage_relations"]["double_damage_from"][i]["name"])

for i in range(len(data1["damage_relations"]["half_damage_from"])):
  print(data1["damage_relations"]["half_damage_from"][i]["name"])

for i in range(len(data2["damage_relations"]["half_damage_from"])):
  print(data2["damage_relations"]["half_damage_from"][i]["name"])