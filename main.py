from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv, dotenv_values
from os import getenv
load_dotenv()

app = Flask(__name__)
config = dotenv_values('.env')
client = MongoClient(getenv('MONGODB_CONNECTION_URL'))

def get_database():
    return client['cmp315-api']

database = get_database()

import routes.index

if __name__ == "__main__":
    app.run(debug=True)