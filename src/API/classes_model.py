import os
import requests
from dotenv import load_dotenv

class API_Owners:
    '''
    Request for Owner Endpoint model
    '''
    def __init__(self):
        self.api_key = self.API_key()
        self.headers = self._headers()

    def API_key(self):
        load_dotenv(override=True)
        return os.getenv('API_AVANTIO')

    def _headers(self):
        return {
            "accept": "application/json",
            "X-Avantio-Auth": self.api_key
        }

    def url(self): 
        return "https://api.avantio.pro/pms/v2/owners?pagination_size=100"

    def API_request(self, url_):
        response = requests.get(url_, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Erro HTTP: {response.status_code}')
            return None 

class Owners():
    '''
    Extract owner atributes 
    '''
    def __init__(self,owners):
        self.owners = owners

    def owner_id(self):
        return self.owners['id']
    
    def owner_name(self):
        first_name = self.owners['name']
        if len(self.owners['surnames']) == 0:
            return first_name
        else:
            surnames = self.owners['surnames']
            surname = " ".join(surnames)
            return first_name + ' '+ surname

    def owner_email(self):
        return self.owners.get('email','')
    
    def owner_phone(self):
        return self.owners.get('phone','')
    
    def id_owner_document(self):
        return self.owners['identityDocumentId']