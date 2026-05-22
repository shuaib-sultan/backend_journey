from flask import request ,g,current_app
from functools import wraps
from app.core.errors import (
  AuthenticationError,
  PermissionError)
from app.utils.jwt_utiles import (
  decode_token,
  extract_token)

def auth_required(fun):
  @wraps(fun)
  def wrapper(*args,**kargs):
    header=request.headers.get("Authorization")
    token=extract_token(header)
    if not token :
      current_app.logger.warning("Unauthorized access attempt")
      raise AuthenticationError("Token is missing")
    payload=decode_token(token)
    if not payload or "id" not in payload or "role_id" not in payload: 
      raise AuthenticationError("Invalid token payload")
    g.user_id=payload["id"]
    g.user_payload=payload
    return fun(*args,**kargs)
  return wrapper

def role_required(*roles):
  def dec(fun):
    @wraps(fun)
    def wrapper(*args,**kargs):
      if not hasattr(g, "user_payload"):
        raise AuthenticationError("Authentication required")
      if g.user_payload["role_id"] not in roles:
        current_app.logger.warning(f"Access denied for user {g.user_id} due to insufficient role")
        raise PermissionError(f"{roles} privileges required")
      return fun(*args,**kargs)
    return wrapper
  return dec
