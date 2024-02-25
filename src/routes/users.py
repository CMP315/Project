from flask import Response, request, jsonify
from __main__ import app
from services.database import get_collection
from bson import json_util
from json import loads
from datetime import datetime
import bcrypt
import bson.errors
from bson.objectid import ObjectId

PATH = "/users/"

users_collection = get_collection("users")

@app.post(PATH)
def users_post():
    data = request.get_json()
    try:
        email:str = data.get('email')
        if not email: raise Exception("email")
    
        password:str = data.get('password')
        if not password: raise Exception("password")
        
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    except Exception as x:
        return jsonify({ "status": False, "message": f"Missing {str(x).upper()} parameter from body."})
    
    created_at = datetime.now()
    
    response = users_collection.insert_one({
        "email": email,
        "password": hashed_password,
        "created_at": created_at,
    })

    if not response.acknowledged: return jsonify({ "status": False, "message": "Request not acknowledged by MongoDB."}) 
    
    return jsonify({
        "_id": loads(json_util.dumps(response.inserted_id))['$oid'],
        "email": email,
        "password": hashed_password,
        "created_at": created_at
    })
    
@app.get(PATH)
def users_get():
    all_users = users_collection.find({})
    users_list = []
    
    for user in all_users:
        user['_id'] = str(user['_id'])
        user.pop('password', None)
        users_list.append(user)
    
    users_json = json_util.dumps(users_list)
    return Response(users_json, mimetype='application/json')

@app.get(PATH + "<user_id>")
def user_get(user_id:str):
    try:
        user = users_collection.find_one({ '_id': ObjectId(user_id) })
        if not user: return jsonify({ "status": False, "message": "User does not exist."}), 400
        print(user)
        user['_id'] = str(user['_id'])
        user = json_util.dumps(user)
        
        return Response(user, mimetype='application/json')
    except bson.errors.InvalidId as e:
        return jsonify({ "status": False, "message": "Invalid User ID is supplied, cannot convert to ObjectId."}), 400