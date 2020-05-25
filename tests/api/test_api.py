import pytest
import requests

class TestAPI:

    base_url = "https://pokeapi.co/api/v2"
    endpoint_pokemon = "/pokemon/bulbasaur/"
    endpoint_type = "/type/poison/"

    expected_name = "bulbasaur"
    expected_type = "poison"
    
    def test_simple_search(self):
        response = requests.get(self.base_url + self.endpoint_pokemon)
        body = response.json()
        name = body["name"]
        assert name == self.expected_name

    def test_simple_type_search(self):
        response = requests.get(self.base_url + self.endpoint_type)
        body = response.json()
        name = body["name"]
        assert name == self.expected_type
        
