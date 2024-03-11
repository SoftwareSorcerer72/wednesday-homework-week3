import requests

class Pokemon:
     def  __init__(self, poke_id, name, height, weight, stats, img_url):
        self.poke_id = poke_id
        self.name = name.title()
        self.height = height
        self.weight = weight
        self.stats = stats
        self.img_url = img_url

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

client = PokemonAPI()

