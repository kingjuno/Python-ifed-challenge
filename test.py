import requests
import json
urll = "http://pokeapi.co/api/v2/pokemon/gyarados/"
urls=[]
data = requests.get(urll).json()
for i in range (2):
    poke_type=data["types"][i]['type']['name']
    urls.append(data["types"][i]['type']['url']) #appending url for step 2
d_dmg_url=[]
tp=[]
for url in urls:
    poke_type=requests.get(url).json()
    for j in poke_type["damage_relations"]["double_damage_from"]:
        d_dmg_url.append(j["url"])
        tp.append(j["name"])
        
for i in range(len(d_dmg_url)):
    dat=requests.get(d_dmg_url[i]).json()
    print("Pokemon of Type: "+tp[i])
    for j in range(5):
        print(dat["pokemon"][j]["pokemon"]["name"],end=',')
    print("\n")