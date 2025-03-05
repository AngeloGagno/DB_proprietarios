from Database.models import Owner
from API.data_model import owner_data
from sqlalchemy.orm import Session

def send_data_to_database(db:Session,data = owner_data()) -> None:
        for owner in data: 
            inserted_data = Owner(
                id_proprietario = owner['id_proprietario'],
                nome = owner['nome'],
                documento = owner['documento'],
                telefone = owner['telefone'],
                email = owner['email']
            )
            db.merge(inserted_data)
        db.commit()