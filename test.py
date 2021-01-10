import requests

url = "http://pokeapi.co/api/v2/pokemon/gyarados/"

data = requests.get(url).json()
for i in range (2):
    poke_type=data["types"][i]['type']['name']
    print(poke_type)
