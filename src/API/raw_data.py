from API.classes_model import API_Owners
import requests
import json

def request_data()-> json:
    api = API_Owners()
    url_api = api.url()
    raw_content = []
    while url_api:
        request = api.API_request(url_= url_api)
        raw_content.extend(request.get('data', [])) 
        url_api = request.get('_links',{}).get('next')
    return raw_content