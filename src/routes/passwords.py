from flask import request, jsonify
from __main__ import app
from services.database import get_collection
from bson import json_util
from json import loads
from datetime import datetime
from bson.objectid import ObjectId
import bson.errors
import bcrypt

PATH = "/passwords/"

passwords_collection = get_collection("passwords")
users_collection = get_collection("users")

@app.post(PATH + "<user_id>")
def passwords_post(user_id:str):
    data = request.get_json()
    try:
        if not user_id: raise Exception("user id")
    
        username:str = data.get('username')
        if not username: raise Exception("username")
    
        password:str = data.get('password')
        if not password: raise Exception("password")
    except Exception as x:
        return jsonify({ "status": False, "message": f"Missing {str(x).upper()} parameter from body."}), 400

    site_name:str = data.get('site_name', None) # Optional
    notes:str = data.get('notes', None) # Optional
    created_at:datetime = datetime.now()
    
    try:
        user = users_collection.find_one({ '_id': ObjectId(user_id) })
        if not user: return jsonify({ "status": False, "message": "User does not exist."}), 400
    except bson.errors.InvalidId as e:
        return jsonify({ "status": False, "message": "Invalid User ID is supplied, cannot convert to ObjectId."}), 400

    response = passwords_collection.insert_one({
        "user_id": user_id,
        "username": username,
        "password": password,
        "created_at": created_at,
        "site_name": site_name,
        "notes": notes
    })

    if not response.acknowledged: return jsonify({ "status": False, "message": "Request not acknowledged by MongoDB."}), 400
    
    return jsonify({
        "_id": loads(json_util.dumps(response.inserted_id))['$oid'],
        "user_id": user_id,
        "username": username,
        "password": password,
        "site_name": site_name,
        "notes": notes,
        "created_at": created_at
    }), 200