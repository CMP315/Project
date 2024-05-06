from flask import Flask, Request, request, jsonify
from os import getenv
from dotenv import load_dotenv
from services.jwt_utils import decode_and_validate_jwt_token

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


load_dotenv()
app = Flask(__name__)
DEBUG = getenv("DEBUG") == "true" or False

import services.database
import routes.index
import routes.users
import routes.passwords
import routes.notes

rsa_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

encrypted_pem_private_key = rsa_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

pem_public_key = rsa_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
)

private_key = '\n'.join(x.decode() for x in encrypted_pem_private_key.splitlines())
public_key = '\n'.join(x.decode() for x in pem_public_key.splitlines())

print("rsa_key[private]:", private_key)
print("rsa_key[public]:", public_key)

def validate_user(request:Request):
    try:
        auth_header = request.headers.get('Authorization', type=str)
        if not auth_header: return False
        print("auth_header:", auth_header)
        payload = decode_and_validate_jwt_token(auth_header, public_key)
        if payload:
            return True
    except:
        return False
    
@app.before_request
def before_request():
    if not request.path.startswith('/ping') and not ((request.path.startswith('/login') or request.path.startswith('/users')) and request.method == "POST"):
        is_validated = validate_user(request)
        if not is_validated: return jsonify({ "status": False, "message": "Invalid Authorization Header. Unauthorized."}), 401
        print("is_validated", is_validated)
    
    log_message = (
        f"\n[ REQUEST RECEIVED: {request.method} {request.path} ]\n"
        f"Request Information:\n"
        f"-------------------\n"
        f"Headers: {request.headers}"
        f"Request Body: {request.data.decode('utf-8')}"
    )
    app.logger.debug(log_message)

if __name__ == "__main__":
    if (getenv("HTTPS") or "false").lower() == "true":
        app.run(debug=DEBUG, port=443, ssl_context=('cert.pem', 'key.pem')) # HTTPS
    else:
        app.run(debug=DEBUG, port=80) # HTTP