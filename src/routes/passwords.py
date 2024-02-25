from __main__ import app, database
from flask import request

PATH = "/passwords/"

@app.route(PATH, methods=['POST'])
def post():
    data = request.get_json()
    return data
