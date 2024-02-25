from flask import Flask
from pymongo import MongoClient
from os import getenv

from dotenv import load_dotenv, dotenv_values
app = Flask(__name__)

load_dotenv()
config = dotenv_values('.env')
DEBUG = False
client = MongoClient(getenv('MONGODB_CONNECTION_URL'))

def get_database():
    return client['cmp315-api']

database = get_database()

import routes.index
import routes.passwords

if getenv("ENVIRONMENT") == "production" or not __name__ == "__main__":
    app.run(debug=DEBUG, ssl_context=('cert.pem', 'key.pem'), port=443) # HTTPS
else:
    app.run(debug=DEBUG, port=80) # HTTP