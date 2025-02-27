
class Owners():
    def __init__(self,json):
        self.json = json
        self.data = self._data()

    def _data(self):
        return self.json['data']

    def owner_id(self):
        return self.data['id']
    
    def owner_name(self):
        first_name = self.data['name']
        if len(self.data['surname']) == 0:
            return first_name
        else:
            surnames = self.data['surname']
            surname = " ".join(surnames)
            return first_name + surname

    def owner_email(self):
        return self.data['email']
    
    def owner_phone(self):
        return self.data.get('phone','')
    
    def id_owner_document(self):
        return self.data['identityDocumentId']