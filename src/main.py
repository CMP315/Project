from flask import Flask, request
from os import getenv
from dotenv import load_dotenv, dotenv_values

load_dotenv()
config = dotenv_values('.env')

app = Flask(__name__)
DEBUG = getenv("DEBUG") == "true" or False

import services.database

import routes.index
import routes.users
import routes.passwords
import routes.notes

if __name__ == "__main__":
    if (getenv("HTTPS") or "false").lower() == "true":
        app.run(debug=DEBUG, port=443, ssl_context=('cert.pem', 'key.pem')) # HTTPS
    else:
        app.run(debug=DEBUG, port=80) # HTTP
        
@app.before_request
def before_request():
    log_message = (
        f"\n[ REQUEST RECEIVED: {request.method} {request.path} ]\n"
        f"Request Information:\n"
        f"-------------------\n"
        f"Headers: {request.headers}"
        f"Request Body: {request.data.decode('utf-8')}"
    )
    app.logger.debug(log_message)