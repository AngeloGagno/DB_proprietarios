import requests
import os
from dotenv import load_dotenv

class API_Owners():
    def __init__(self):
        self.api_key = self.API_key()
        
    
    def API_key(self):
        load_dotenv(override=True)
        return os.getenv('API_AVANTIO')
    def _headers(self):
        headers = {
    "accept": "application/json",
    "X-Avantio-Auth": self.api_key
}