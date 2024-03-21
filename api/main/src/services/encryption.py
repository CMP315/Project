import os
import bcrypt
import bson
import bson.errors
from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Protocol.KDF import PBKDF2
from services.database import get_collection

passwords_collection = get_collection("passwords")
users_collection = get_collection("users")

def derive_keys(master_password, salt):
    keys = PBKDF2(master_password, salt, dkLen=32)
    return keys[:16], keys[16:]

def process_password(password, aes_key, hmac_key):
    if not password: print("Missing Password"); return [None, None, None]
    if not aes_key: print("Missing AES Key");return [None, None, None]
    if not hmac_key: print("Missing HMAC Key");return [None, None, None]
    
    nonce = os.urandom(8)
    cipher = AES.new(aes_key, AES.MODE_CTR, nonce=nonce)
    ciphertext = cipher.encrypt(password.encode())
    hmac = HMAC.new(hmac_key, digestmod=SHA256)
    hmac.update(nonce + ciphertext)
    tag = hmac.digest()
    return tag, nonce, ciphertext

def authenticate_and_decrypt(tag, nonce, ciphertext, aes_key, hmac_key):
    hmac_calc = HMAC.new(hmac_key, digestmod=SHA256)
    hmac_calc.update(nonce + ciphertext)
    try:
        hmac_calc.verify(tag)
        cipher = AES.new(aes_key, AES.MODE_CTR, nonce=nonce)
        return cipher.decrypt(ciphertext).decode()
    except ValueError:
        return None
    
def encrypt_password(user_id, password_to_encrypt, master_password=None, salt=None):
    try:
        user = users_collection.find_one({ "_id": bson.ObjectId(user_id) })
        if master_password and salt:
            aes_key, hmac_key = derive_keys(master_password, salt)
        else:
            print(user)
            if not user or not user['salt'] or not user['password']: return None
            aes_key, hmac_key = derive_keys(user['password'], user['salt'])
            print(user)
            print(aes_key, hmac_key)
        tag, nonce, ciphertext = process_password(password_to_encrypt, aes_key, hmac_key)
        return f"{tag}?+?{nonce}?+?{ciphertext}"
    except bson.errors.InvalidId as e:
        return None
    
def decrypt_password(user_id, password_to_decrypt, master_password=None, salt=None):
    if master_password and salt:
        aes_key, hmac_key = derive_keys(master_password, salt)
    else:
        user = users_collection.find_one({ "_id": bson.ObjectId(user_id) })
        if not user or not user['salt']: return None
        aes_key, hmac_key = derive_keys(user['password'], user['salt'])
    
    tag_str, nonce_str, ciphertext_str = password_to_decrypt.split('?+?')

    
    tag = eval(tag_str)
    nonce = eval(nonce_str)
    ciphertext = eval(ciphertext_str)
    if tag:
        decrypted_password = authenticate_and_decrypt(tag, nonce, ciphertext, aes_key, hmac_key)
        if decrypted_password:
            return decrypted_password