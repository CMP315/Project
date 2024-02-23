from __main__ import app, database

@app.route('/')
def ping():    
    return "API is online."
