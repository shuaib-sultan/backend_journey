import jwt
from datetime import datetime,timezone,timedelta
from app.utils.validators import (check_email,check_empty,check_password)
from app.models.user_model import(get_user_by_email,get_user_by_id)
from app.core.errors import ValidationError
from app.utils.response import success
from app.config import get_secret_key

def login_logic(user_data):
  email=user_data.get("user_email")
  password=user_data.get("password")
  check_empty(email,password,"Email and password are required.")
  check_password(password)
  user=get_user_by_email(email)
  if not user:
    raise ValidationError("Emial is not found ")
  if user[0]["password"] != password :
    raise ValidationError("Invalid password")
  payload={
    "user_id":user[0]["id"],
    "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
}
  SECRET_KEY=get_secret_key()["secret"]
  token = jwt.encode(payload,SECRET_KEY,algorithm="HS256")
  return success("Login successfully.",token)

