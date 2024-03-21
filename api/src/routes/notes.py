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

PATH = "/notes/"

notes_collection = get_collection("notes")
users_collection = get_collection("users")

@app.post(PATH + "<user_id>")
def notes_post(user_id:str):
    try:
        data = request.get_json()
        try:
            if not user_id: raise Exception()
    
            name:str = data.get('name')
            if not name: raise Exception()
    
            note:str = data.get('note')
            if not note: raise Exception()
        except Exception as x:
            return jsonify({ "status": False, "message": f"Missing required parameter from body."}), 400

        encrypted_name = encrypt_password(user_id, name)
        encrypted_note = encrypt_password(user_id, note)
        if not encrypted_name: return jsonify({ "status": False, "message": "Issue encrypting Note Name."}), 500
        if not encrypted_note: return jsonify({ "status": False, "message": "Issue encrypting Note Content."}), 500
    
        created_at:datetime = datetime.now()
        last_edited_at = None
    
        user = users_collection.find_one({ '_id': ObjectId(user_id) })
        if not user: return jsonify({ "status": False, "message": "User does not exist."}), 404

        response = notes_collection.insert_one({
            "user_id": user_id,
            "name": encrypted_name,
            "note": encrypted_note,
            "created_at": created_at,
            "last_edited_at": last_edited_at
        })

        if not response.acknowledged: return jsonify({ "status": False, "message": "Request not acknowledged by MongoDB."}), 400
    
        return jsonify({
            "_id": loads(json_util.dumps(response.inserted_id))['$oid'],
            "user_id": user_id,
            "name": encrypted_name,
            "note": encrypted_note,
            "created_at": created_at,
            "last_edited_at": last_edited_at
        }), 200
    except bson.errors.InvalidId as e:
            return jsonify({ "status": False, "message": "Invalid User ID is supplied, cannot convert to ObjectId."}), 400
    
@app.get(PATH + "<user_id>")
def notes_get_all(user_id:str):
    try:
        all_notes = notes_collection.find({ "user_id": user_id })
        if not all_notes: return jsonify({ "status": False, "message": "No Notes Found." }), 404
        note_list = []

        for note in all_notes:
            note['_id'] = str(note['_id'])
            note['name'] = decrypt_password(user_id, note.pop('name', None))
            note.pop('note', None)
            note_list.append(note)

        return jsonify(note_list)
    except bson.errors.InvalidId as e:
            return jsonify({ "status": False, "message": "Invalid User ID is supplied, cannot convert to ObjectId."}), 400

@app.get(PATH + "<user_id>/<note_id>")
def notes_get(user_id:str, note_id:str):
    try:
        note = notes_collection.find_one({ "user_id": user_id, "_id": ObjectId(note_id) })
        if not note: return jsonify({ "status": False, "message": "No Note Found." }), 404
        
        note['_id'] = str(note['_id'])
        note['name'] = decrypt_password(user_id, note.pop('name', None))
        note['note'] = decrypt_password(user_id, note.pop('note', None))
        
        return jsonify(note)
    except bson.errors.InvalidId as e:
            return jsonify({ "status": False, "message": "Invalid User ID is supplied, cannot convert to ObjectId."}), 400


@app.patch(PATH + "<user_id>/<note_id>")
def notes_patch(user_id:str, note_id:str):
    try:
        db_note = notes_collection.find_one({ "user_id": user_id, "_id": ObjectId(note_id) })
        if not db_note: return jsonify({ "status": False, "message": "Note not found." }), 404

        data = request.get_json()
        
        name:str = data.get('name', None)
        if name:
            encrypted_name = encrypt_password(user_id, name)
            if not encrypted_name: return jsonify({ "status": False, "message": "Issue encrypting note name."}), 500
            db_note['name'] = encrypted_name
        
        note:str = data.get('note', None)
        if note:
            encrypted_note = encrypt_password(user_id, note)
            if not encrypted_note: return jsonify({ "status": False, "message": "Issue encrypting note content."}), 500
            db_note['note'] = encrypted_note

        
        db_note['last_edited_at'] = datetime.now()
        response = notes_collection.replace_one({ "_id": ObjectId(note_id)}, db_note, True)
        # if not response.acknowledged or response.modified_count == 0: return jsonify({ "status": False, "message": "Not saved to MongoDB"}), 500
        # return jsonify(db_password)
        db_note['_id'] = str(db_note['_id'])
        if response.acknowledged and response.matched_count > 0:
            return jsonify(db_note), 200
        else:
            return jsonify({ "status": False, "message": "Not saved to MongoDB"}), 500
    except bson.errors.InvalidId as e:
            return jsonify({ "status": False, "message": "Invalid User ID is supplied, cannot convert to ObjectId."}), 400

@app.delete(PATH + "<user_id>")
def notes_delete_all(user_id:str):
    try:
        response = notes_collection.delete_many({ "user_id": user_id })
        if not response.acknowledged: return jsonify({ "status": False, "message": "Request not acknowledged by MongoDB." }), 500
        if not response.deleted_count > 0: return jsonify({ "status": False, "message": "No documents deleted." }), 401
        return jsonify({ "status": True })
    except bson.errors.InvalidId as e:
            return jsonify({ "status": False, "message": "Invalid User ID is supplied, cannot convert to ObjectId."}), 400
        
@app.delete(PATH + "<user_id>/<note_id>")
def notes_delete(user_id:str, note_id:str):
    try:
        response = notes_collection.delete_one({ "user_id": user_id, "_id": ObjectId(note_id) })
        if not response.acknowledged: return jsonify({ "status": False, "message": "Request not acknowledged by MongoDB." }), 500
        if not response.deleted_count > 0: return jsonify({ "status": False, "message": "No documents deleted." }), 401
        return jsonify({ "status": True })
    except bson.errors.InvalidId as e:
            return jsonify({ "status": False, "message": "Invalid User ID is supplied, cannot convert to ObjectId."}), 400