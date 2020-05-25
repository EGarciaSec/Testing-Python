import pytest
import requests
from core.api.api_requests import APIRequests

class TestAPI:

    expected_name = "bulbasaur"
    expected_type = "poison"
    
    def test_simple_search(self):
        body = APIRequests().pokemon_search(self.expected_name)
        name = body["name"]
        assert name == self.expected_name

    def test_simple_type_search(self):
        body = APIRequests().type_search(self.expected_type)
        name = body["name"]
        assert name == self.expected_type
        
