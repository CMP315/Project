from pymongo import MongoClient
from os import getenv

client = MongoClient(getenv('MONGODB_CONNECTION_URL'))

def get_database(name:str):
    print("[database] fetching database")
    return client[name]

database_name = getenv('DATABASE_NAME')
if not database_name: raise Exception("Database Name Missing from Environment Variables, unable to connect.")
database = get_database(str(database_name))

def get_collection(name:str):
    print("[database] fetching collection")
    return database.get_collection(name)
