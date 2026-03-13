from functools import wraps
from flask import g,request
from app.config import get_secret_key
from app.core.errors import AuthenticationError
import jwt
from jwt import InvalidTokenError,ExpiredSignatureError

def get_token_from_header():
  headr=request.headers.get("Authorization")
  if not headr:
    return None
  headr=headr.split()
  if len(headr)!=2:
    return None
  schema=headr[0]
  token=headr[1]
  if schema.lower() !="bearer":
    return None
  return token

def decode_the_token(token):
  secret=get_secret_key()["secret"]
  if not secret:
    raise AuthenticationError("Server misconfiguration: SECRET_KEY is missing.",500, None)
  try:
    payload = jwt.decode(token, secret, algorithms=["HS256"])
    return payload
  except ExpiredSignatureError:
        raise AuthenticationError("Token has expired.",404, None)
  except InvalidTokenError:
        raise AuthenticationError("Invalid token.",404, None)
  except Exception:
        raise AuthenticationError("Failed to decode token.",404, None)

def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = get_token_from_header()
        if not token:
            raise AuthenticationError("Authorization header with Bearer token required.",404, None)
        payload = decode_the_token(token)
        g.current_user_payload = payload
        g.current_user_id = payload.get("user_id") or payload.get("sub")
        return func(*args, **kwargs)
    return wrapper

def auth_admin(fun):
    @wraps(fun)
    def warper(*arg,**karg):
        if g.current_user_payload.get("role") != "admin":
            raise AuthenticationError("Admin privileges required.")
        return fun(*arg,**karg)
    return warper

