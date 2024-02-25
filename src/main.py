from flask import Flask
from os import getenv
from dotenv import load_dotenv, dotenv_values


load_dotenv()
config = dotenv_values('.env')


app = Flask(__name__)
DEBUG = True

import services.database
import routes.index
import routes.passwords

if __name__ == "__main__":
    if (getenv("HTTPS") or "false").lower() == "true":
        app.run(debug=DEBUG, port=443, ssl_context=('cert.pem', 'key.pem')) # HTTPS
    else:
        app.run(debug=DEBUG, port=80) # HTTP
