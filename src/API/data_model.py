from API.raw_data import request_data
from API.classes_model import Owners
import json 

def owner_data(api:json= request_data()) -> json:
    owners_normalized = []
    for owner_detail in api:
        owner = Owners(owners=owner_detail)
        id = owner.owner_id()
        name = owner.owner_name()
        id_owner_document = owner.id_owner_document()
        phone = owner.owner_phone()
        email = owner.owner_email()
        owners_normalized.append({'id_proprietario':id,'nome':name,'documento':id_owner_document,
        'telefone':phone,'email':email})
    return owners_normalized