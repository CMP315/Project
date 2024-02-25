from __main__ import app

PATH = "/"

@app.route(PATH + 'ping', methods=['GET'])
def ping():    
    return "API is online."

@app.route(PATH, methods=['GET'])
def index():
    return ping()
