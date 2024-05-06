from flask import Response, request, jsonify
from __main__ import app
from services.database import get_collection
from bson import json_util
from json import loads
from datetime import datetime
import bcrypt
import bson.errors
from secrets import token_hex
from bson.objectid import ObjectId
import re
from os import getenv

from services.encryption import decrypt_password, encrypt_password
from services.jwt_utils import generate_jwt_token
from utils import is_url_image
from main import private_key

PATH = "/users/"

users_collection = get_collection("users")
passwords_collection = get_collection("passwords")
notes_collection = get_collection("notes")

@app.post(PATH)
def users_post():
    data = request.get_json()
    try:
        name:str = data.get('name')
        if not name: raise Exception()
        
        email:str = data.get('email')
        if not email: raise Exception()
    
        password:str = data.get('password')
        if not password: raise Exception()
        
        salt = bcrypt.gensalt()
        
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")

    except Exception as x:
        return jsonify({ "status": False, "message": f"Missing required parameter from body."})

    image:str = data.get('image', None)
    if image is not None and is_url_image(image) == False: return jsonify({ "status": False, "message": f"Invalid Image URL in body"})
    
    created_at = datetime.now()
    
    user = {
        "name": name,
        "image": image,
        "email": email,
        "password": hashed_password,
        "salt": salt,
        "created_at": created_at,
    }
    response = users_collection.insert_one(user)
    
    if not response.acknowledged: return jsonify({ "status": False, "message": "Request not acknowledged by MongoDB."}) 
    
    user.pop("password")
    user.pop("salt")
    user['_id'] = str(
        loads(
            json_util.dumps(response.inserted_id))['$oid'])
    
    user_session_id = token_hex(16)
    user_jwt_token = generate_jwt_token(user['_id'], user_session_id, private_key)
    
    payload = json_util.dumps({
        "user": user,
        "jwt": user_jwt_token,
    })
    
    return Response(payload, mimetype='application/json')
    
@app.post("/login")
def users_login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        user = users_collection.find_one({ 'email': email })
        print(user)
        if not user: return jsonify({ "status": False, "message": "User does not exist."}), 400
        
        isvalid = bcrypt.checkpw(str.encode(password), str.encode(user['password']))
        if not isvalid: return jsonify({"status": False, "message": "Invalid Login Credentials"}), 401
        
        user.pop("password")
        user.pop("salt")
        user['_id'] = str(user['_id'])
        user['created_at'] = str(loads(json_util.dumps(user['created_at']))['$date'])
        
        user_session_id = token_hex(16)
        user_jwt_token = generate_jwt_token(user['_id'], user_session_id, private_key)

        payload = json_util.dumps({
            "user": user,
            "jwt": user_jwt_token,
        })
        
        return Response(payload, mimetype='application/json')
    except bson.errors.InvalidId as e:
        return jsonify({ "status": False, "message": "Invalid User ID is supplied, cannot convert to ObjectId."}), 400
    
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
        user['_id'] = str(user['_id'])
        user = json_util.dumps(user)
        
        return Response(user, mimetype='application/json')
    except bson.errors.InvalidId as e:
        return jsonify({ "status": False, "message": "Invalid User ID is supplied, cannot convert to ObjectId."}), 400

@app.patch(PATH + "<user_id>")
def user_path(user_id:str):
    try:
        user = users_collection.find_one({ '_id': ObjectId(user_id) })
        if not user: return jsonify({ "status": False, "message": "User does not exist. Use POST method instead."}), 400
        data = request.get_json()
        
        try:
            name:str = data.get('name')
            if name:
                user['name'] = name
        except:
            pass
        
        try:
            email_regex = "^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$" # type: ignore
            email:str = data.get('email')
            if email and re.search(email_regex, email):
                user['email'] = email
        except:
            pass
        
        try:
            image:str = data.get('image')
            if image and is_url_image(image):
                user['image'] = image
        except:
            pass
        
        # try:
        master_password = data.get('password', None)
        if master_password:
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(master_password.encode("utf-8"), salt).decode("utf-8")
            
            old_hashed_password = user['password']
            old_salt = user['salt']
            new_hashed_password = str(hashed_password)
            new_salt = str(salt)

            user['password'] = new_hashed_password
            user['salt'] = new_salt

            all_accounts = passwords_collection.find({ "user_id": user_id })            
            if all_accounts:
                for account in all_accounts:
                    decrypted_password = decrypt_password(user_id, account['password'], old_hashed_password, old_salt)
                    account['password'] = encrypt_password(user_id, decrypted_password, new_hashed_password, new_salt)
                    passwords_collection.replace_one({"_id": ObjectId(account['_id'])}, account, True)
            
            all_notes = notes_collection.find({ "user_id": user_id })
            if all_notes:
                for note in all_notes:
                    decrypted_name = decrypt_password(user_id, note['name'], old_hashed_password, old_salt)
                    decrypted_note = decrypt_password(user_id, note['note'], old_hashed_password, old_salt)
                    
                    note['name'] = encrypt_password(user_id, decrypted_name, new_hashed_password, new_salt)
                    note['note'] = encrypt_password(user_id, decrypted_note, new_hashed_password, new_salt)
                    
                    notes_collection.replace_one({"_id": ObjectId(note['_id'])}, note, True)

        users_collection.replace_one({ "_id": ObjectId(user_id) }, user, True)
        user['_id'] = str(user['_id'])
        return jsonify(user)
    except bson.errors.InvalidId as e:
        return jsonify({ "status": False, "message": "Invalid User ID is supplied, cannot convert to ObjectId."}), 400
    

@app.delete(PATH + "<user_id>")
def user_delete(user_id:str):
    try:
        response = users_collection.delete_one({ '_id': ObjectId(user_id) })
        if not response.deleted_count > 0: return jsonify({ "status": False, "message": "No User with that ID found."}), 404
        return jsonify({ "status": True })
    except bson.errors.InvalidId as e:
        return jsonify({ "status": False, "message": "Invalid User ID is supplied, cannot convert to ObjectId."}), 400
        