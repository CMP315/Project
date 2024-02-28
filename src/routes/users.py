from flask import Response, request, jsonify
from __main__ import app
from services.database import get_collection
from bson import json_util
from json import loads
from datetime import datetime
import bcrypt
import bson.errors
from bson.objectid import ObjectId
import re

from services.encryption import decrypt_password, encrypt_password

PATH = "/users/"

users_collection = get_collection("users")
passwords_collection = get_collection("passwords")

@app.post(PATH)
def users_post():
    data = request.get_json()
    try:
        name:str = data.get('name')
        if not name: raise Exception("name")
        
        email:str = data.get('email')
        if not email: raise Exception("email")
    
        password:str = data.get('password')
        if not password: raise Exception("password")
        
        salt = bcrypt.gensalt()
        
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")

    except Exception as x:
        return jsonify({ "status": False, "message": f"Missing {str(x).upper()} parameter from body."})
    
    created_at = datetime.now()
    
    response = users_collection.insert_one({
        "name": name,
        "email": email,
        "password": hashed_password,
        "salt": salt,
        "created_at": created_at,
    })

    if not response.acknowledged: return jsonify({ "status": False, "message": "Request not acknowledged by MongoDB."}) 
    
    return jsonify({
        "_id": loads(json_util.dumps(response.inserted_id))['$oid'],
        "name": name,
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
            email_regex = "^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
            email:str = data.get('email')
            if email and re.search(email_regex, email):
                user['email'] = email
        except:
            pass
        
        # try:
        master_password = data.get('password', None)
        if master_password:
            all_accounts = passwords_collection.find({ "user_id": user_id })
            if not all_accounts: return jsonify({ "status": False, "message": "No Passwords Found." }), 404

            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(master_password.encode("utf-8"), salt).decode("utf-8")
            
            old_hashed_password = user['password']
            old_salt = user['salt']
            new_hashed_password = str(hashed_password)
            new_salt = str(salt)
            
            for account in all_accounts:
                print(account)
                print("Decrypting password")
                # try:
                decrypted_password = decrypt_password(user_id, account['password'], old_hashed_password, old_salt)
                # except:
                    # print("error decrypting")
                print(f"Decrypting password...............{decrypted_password}")
                print("Re-encrypting password")
                account['password'] = encrypt_password(user_id, decrypted_password, new_hashed_password, new_salt)
                print(f"Re-encrypting password...............{account['password']}")
                passwords_collection.replace_one({"_id": ObjectId(account['_id'])}, account, True)
            print(all_accounts)
            # /return response
            
            user['password'] = new_hashed_password
            user['salt'] = new_salt
        # except:
            # pass
            
        users_collection.replace_one({ "_id": ObjectId(user_id) }, user, True)
        # try:
        #     password:str = data.get('password')
        #     if password:
        #         old_password = user['password']
                
        #         passwords = passwords_collection.find({ 'user_id': ObjectId(user_id) })
        #         new_passwords = []
                
        #         for child in passwords:
        #             bcrypt
                
        #         new_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        #         user['password'] = new_password
        # except:
        #     pass
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
        