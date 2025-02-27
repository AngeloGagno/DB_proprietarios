from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os 

def db_url():
    load_dotenv(override=True)
    return os.getenv('Database_url')

engine = create_engine(db_url())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    
    db = SessionLocal()
    
    try:
        return db
    except:
        db.close()