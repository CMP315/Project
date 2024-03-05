from flask import request, jsonify
from __main__ import app
from services.database import get_collection
from bson import json_util
from json import loads
from datetime import datetime
from bson.objectid import ObjectId
import bson.errors
import bcrypt

from services.encryption import decrypt_password, encrypt_password

PATH = "/passwords/"

passwords_collection = get_collection("passwords")
users_collection = get_collection("users")

@app.post(PATH + "<user_id>")
def passwords_post(user_id:str):
    try:
        data = request.get_json()
        try:
            if not user_id: raise Exception("user id")
    
            username:str = data.get('username')
            if not username: raise Exception("username")
    
            password:str = data.get('password')
            if not password: raise Exception("password")
        
            site_name:str = data.get('site_name')
            if not site_name: raise Exception("site_name")

        except Exception as x:
            return jsonify({ "status": False, "message": f"Missing {str(x).upper()} parameter from body."}), 400

        encrypted_password = encrypt_password(user_id, password)
        if not encrypted_password: return jsonify({ "status": False, "message": "Issue encrypting password."}), 500
    
        notes:str = data.get('notes', None) # Optional
        created_at:datetime = datetime.now()
        last_edited_at = None
    
        user = users_collection.find_one({ '_id': ObjectId(user_id) })
        if not user: return jsonify({ "status": False, "message": "User does not exist."}), 404

        response = passwords_collection.insert_one({
            "user_id": user_id,
            "username": username,
            "password": encrypted_password,
            "created_at": created_at,
            "last_edited_at": last_edited_at,
            "site_name": site_name,
            "notes": notes
        })

        if not response.acknowledged: return jsonify({ "status": False, "message": "Request not acknowledged by MongoDB."}), 400
    
        return jsonify({
            "_id": loads(json_util.dumps(response.inserted_id))['$oid'],
            "user_id": user_id,
            "username": username,
            "password": encrypted_password,
            "site_name": site_name,
            "notes": notes,
            "created_at": created_at,
            "last_edited_at": last_edited_at
        }), 200
    except bson.errors.InvalidId as e:
            return jsonify({ "status": False, "message": "Invalid User ID is supplied, cannot convert to ObjectId."}), 400
    
@app.get(PATH + "<user_id>/<site_id>")
def passwords_get(user_id:str, site_id:str):
    try:
        password = passwords_collection.find_one({ "user_id": user_id, "_id": ObjectId(site_id) })
        if not password: return jsonify({ "status": False, "message": "Password not found." }), 404
        password['_id'] = str(password['_id'])
        password['password'] = decrypt_password(user_id, password['password'])
        return jsonify(password), 200
    except bson.errors.InvalidId as e:
            return jsonify({ "status": False, "message": "Invalid User ID is supplied, cannot convert to ObjectId."}), 400
    
@app.get(PATH + "<user_id>")
def accounts_get(user_id:str):
    try:
        all_accounts = passwords_collection.find({ "user_id": user_id })
        if not all_accounts: return jsonify({ "status": False, "message": "No Passwords Found." }), 404
        users_list = []

        for user in all_accounts:
            user['_id'] = str(user['_id'])
            user.pop('password', None)
            users_list.append(user)

        return jsonify(users_list)
    except bson.errors.InvalidId as e:
            return jsonify({ "status": False, "message": "Invalid User ID is supplied, cannot convert to ObjectId."}), 400

@app.patch(PATH + "<user_id>/<site_id>")
def passwords_patch(user_id:str, site_id:str):
    try:
        db_password = passwords_collection.find_one({ "user_id": user_id, "_id": ObjectId(site_id) })
        if not db_password: return jsonify({ "status": False, "message": "Password not found." }), 404

        data = request.get_json()
        username:str = data.get('username', None)
        if username: db_password['username'] = username

        password:str = data.get('password', None)
        if password:
            encrypted_password = encrypt_password(user_id, password)
            if not encrypted_password: return jsonify({ "status": False, "message": "Issue encrypting password."}), 500
            db_password['password'] = encrypted_password

        site_name:str = data.get('site_name', None)
        if site_name: db_password['site_name'] = site_name

        notes:str = data.get('notes', None)
        if notes: db_password['notes'] = notes

        db_password['last_edited_at'] = datetime.now()
        response = passwords_collection.replace_one({ "_id": ObjectId(site_id)}, db_password, True)
        # if not response.acknowledged or response.modified_count == 0: return jsonify({ "status": False, "message": "Not saved to MongoDB"}), 500
        # return jsonify(db_password)
        db_password['_id'] = str(db_password['_id'])
        if response.acknowledged and response.matched_count > 0:
            return jsonify(db_password), 200
        else:
            return jsonify({ "status": False, "message": "Not saved to MongoDB"}), 500
    except bson.errors.InvalidId as e:
            return jsonify({ "status": False, "message": "Invalid User ID is supplied, cannot convert to ObjectId."}), 400

@app.delete(PATH + "<user_id>")
def passwords_delete_all(user_id:str):
    try:
        response = passwords_collection.delete_one({ "user_id": user_id })
        if not response.acknowledged: return jsonify({ "status": False, "message": "Request not acknowledged by MongoDB." }), 500
        if not response.deleted_count > 0: return jsonify({ "status": False, "message": "No documents deleted." }), 401
        return jsonify({ "status": True })
    except bson.errors.InvalidId as e:
            return jsonify({ "status": False, "message": "Invalid User ID is supplied, cannot convert to ObjectId."}), 400
        
@app.delete(PATH + "<user_id>/<site_id>")
def passwords_delete(user_id:str, site_id:str):
    try:
        response = passwords_collection.delete_one({ "user_id": user_id, "_id": ObjectId(site_id) })
        if not response.acknowledged: return jsonify({ "status": False, "message": "Request not acknowledged by MongoDB." }), 500
        if not response.deleted_count > 0: return jsonify({ "status": False, "message": "No documents deleted." }), 401
        return jsonify({ "status": True })
    except bson.errors.InvalidId as e:
            return jsonify({ "status": False, "message": "Invalid User ID is supplied, cannot convert to ObjectId."}), 400