import requests
from ascii_magic import AsciiArt
class Pokemon:
    def  __init__(self, poke_id, name, height, weight, stats, img_url):
        self.poke_id = poke_id
        self.name = name.title()
        self.height = height
        self.weight = weight
        self.stats = stats
        self.img_url = img_url

    def __repr__(self):
        return f'Pokemon: {self.id} | {self.name}'

    def __str__(self):
        art = AsciiArt.from_url(self.img_url)
        art_string = art.to_ascii()
        return f"{art_string}/nName: {self.poke_id}/nHeight: {self.height}/nWeight: {self.weight}/nStats: {self.stats}"

class PokemonAPI:
    main_url = "https://pokeapi.co/api/v2/"

    def __get(self, endpoint, id_or_name):
        request_url = self.main_url + endpoint + '/' + id_or_name
        response = requests.get(request_url)
        if response.ok:
            return response.json()
        else:
            return None
    
    def get_info(self, pokemon_name):
        
        info = self.__get('pokemon', pokemon_name.lower())
        if info:
            poke_id = info.get('id')
            name = info.get('name')
            height = info.get('height')
            weight = info.get('weight')
            stats = info.get('stats')
            img_url = info.get('sprites').get('front_default')
            new_pokemon = Pokemon(poke_id, name, height, weight, stats, img_url)
            return new_pokemon


client = PokemonAPI()

while True:
    poke_id = input("Enter a Pokemon name: ")
    if poke_id == 'exit':
        break
    pokemon = client.get_info(poke_id)
    print(pokemon)

