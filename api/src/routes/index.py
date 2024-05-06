from __main__ import app

from .passwords import passwords_collection

PATH = "/"

@app.get(PATH + 'ping')
def ping():    
    return "API is online.", 200

@app.get(PATH)
def index():
    return ping()