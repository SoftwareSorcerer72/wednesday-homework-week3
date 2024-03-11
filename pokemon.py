import requests

class PokemonAPI:
    main_url = "https://pokeapi.co/api/v2/"

    def __get(self, endpoint, id_or_name):
        request_url = self.main_url + endpoint + '/' + id_or_name
        return request_url
    
client = PokemonAPI()

