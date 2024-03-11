import requests

class PokemonAPI:
    main_url = "https://pokeapi.co/api/v2/"

    def __get(self, endpoint, id_or_name):
        request_url = self.main_url + endpoint + '/' + id_or_name
        response = requests.get(request_url)
        if response.ok:
            return response.json()
        else:
            return None
    
client = PokemonAPI()

