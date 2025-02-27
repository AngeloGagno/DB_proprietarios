from API.data_model import owner_data
from Fetch.commit import send_data_to_database
from Database.database import get_db,Base,engine
def main():
    session_database = get_db() # Create a session on database 
    Base.metadata.create_all(engine) #Create table is not exists
    send_data_to_database(db=session_database) # Insert all extrated data

if __name__ == '__main__':
    main()