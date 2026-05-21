import uuid

from app.config import get_jwt_key
import jwt 
from uuid import uuid4
from datetime import datetime,timezone,timedelta
from app.core.errors import AuthenticationError
def generate_jwt(user_id,role_id):
  payload={
    "id":user_id,
    "role_id":role_id,
    "jti": str(uuid4()),
    "exp": datetime.now(timezone.utc) + timedelta(minutes=15)
  }
  SECRET_KEY=get_jwt_key()
  token = jwt.encode(payload,SECRET_KEY,algorithm="HS256")
  return token

def extract_token(header):
  if not header :
    return None
  header=header.split()
  if len(header)!=2:
    return None
  schema=header[0]
  token=header[1]
  if schema.lower() != "bearer":
    return None
  return token

from jwt import InvalidTokenError,ExpiredSignatureError

def decode_token(token):
  SECRET_KEY=get_jwt_key()
  if not SECRET_KEY:
    raise AuthenticationError("Server misconfiguration: SECRET_KEY is missing.",500, None)
  try:
    pyload=jwt.decode(token,SECRET_KEY,algorithms="HS256")
    return pyload;
  except ExpiredSignatureError:
        raise AuthenticationError("Token has expired.",404, None)
  except InvalidTokenError:
        raise AuthenticationError("Invalid token.",404, None)
  except Exception:
        raise AuthenticationError("Failed to decode token.",404, None)


