import requests

class APIRequests:
    base_url = "https://pokeapi.co/api/v2"
    endpoint_pokemon = "{}/pokemon/{}/"
    endpoint_type = "{}/type/{}/"

    def pokemon_search(self, name):
        response = requests.get(self.endpoint_pokemon.format(self.base_url, name))
        return response.json()

    def type_search(self, name):
        response = requests.get(self.endpoint_type.format(self.base_url, name))
        return response.json()

        
