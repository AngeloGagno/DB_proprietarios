from sqlalchemy import Column, String
from Database.database import Base

class Owner(Base):
    __tablename__ ='owner'
    id_proprietario = Column(String,primary_key=True)
    nome = Column(String)
    documento = Column(String)
    telefone = Column(String)
    email = Column(String)