import requests
import json

base_url = "https://pokeapi.co/api/v2/pokemon?limit=1000/"

headers = {
    'Content-Type': 'application/json'
}


def json_to_file(response_json):
    cache_file = open('pokemon.json',"w")
    cache_file.write(str(json.dumps(response_json)))
    cache_file.close()

def load_cache():
    response = requests.request("GET",base_url,headers=headers)
    json_to_file(response_json=response.json())

def print_cache():
    cache_res = open("pokemon.json","r")
    data = json.load(cache_res)
    for i in data["results"]:
        print(i["name"],i["url"])

if __name__ == '__main__':
    load_cache()
    print_cache()