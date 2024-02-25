from flask import request, jsonify
from __main__ import app
from services.database import get_collection
from bson import json_util
from json import loads
from datetime import datetime

PATH = "/passwords/"

passwords_collection = get_collection("passwords")

@app.route(PATH + "<user_id>", methods=['POST'])
def post(user_id:str):
    data = request.get_json()
    try:
        if not user_id: raise Exception("user id")
    
        username:str = data.get('username')
        if not username: raise Exception("username")
    
        password:str = data.get('password')
        if not password: raise Exception("password")
    except Exception as x:
        return jsonify({ "status": False, "message": f"Missing {str(x).upper()} parameter from body."})

    site_name:str|None = data.get('site_name', None) # Optional
    notes:str|None = data.get('notes', None) # Optional
    created_at:datetime = datetime.now()
        
    
    response = passwords_collection.insert_one({
        "user_id": user_id,
        "username": username,
        "password": password,
        "created_at": created_at,
        "site_name": site_name,
        "notes": notes
    })

    if not response.acknowledged: return jsonify({ "status": False, "message": "Request not acknowledged by MongoDB."}) 
    
    return jsonify({
        "_id": loads(json_util.dumps(response.inserted_id))['$oid'],
        "user_id": user_id,
        "username": username,
        "password": password,
        "site_name": site_name,
        "notes": notes,
        "created_at": created_at
    })