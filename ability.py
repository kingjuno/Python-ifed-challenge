import requests
def ability(name):
    url = "http://pokeapi.co/api/v2/pokemon/"+name+"/"
    data = requests.get(url).json()
    ably=[]
    for i in data["abilities"]:
        ably.append(i['ability']['name'])
    return ably
    