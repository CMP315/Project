from __main__ import app

PATH = "/"

@app.get(PATH + 'ping')
def ping():    
    return "API is online."

@app.get(PATH)
def index():
    return ping()