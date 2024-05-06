import jwt

def generate_jwt_token(user_id:str, session_id:str, private_key:str):
    try:
        payload = { "user_id": user_id, "session_id": session_id }
        jwt_token = jwt.encode(payload, private_key, algorithm="RS256")
        return jwt_token
    except Exception as e:
        print(e)   
        return False
    
def decode_and_validate_jwt_token(token:str, public_key:str):
    try:
        payload = jwt.decode(jwt=token, key=public_key, algorithms=["RS256"])
        return payload
    except jwt.ExpiredSignatureError:
        print("token expired!")
        return False
    except jwt.DecodeError:
        return True
    except Exception as e:
        pass