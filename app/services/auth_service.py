import jwt
from datetime import datetime,timezone,timedelta
from app.utils.validators import (check_email,check_empty,check_password,check_type,check_syntax)
from app.models.user_model import(get_user_by_email,add_uesr)
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

def sign_up_logic(user_data):
  check_type(user_data)
  check_syntax(user_data)
  check_empty(**user_data)
  email=user_data["email"]
  check_email(email)
  password=user_data["password"]
  check_password(password)
  user=get_user_by_email(email)
  if user:
    raise ValidationError("This user is already in the system  log in to get your new token .")
  new_user=add_uesr(user_data)
  payload={
    "user_id":new_user,
    "role":"user",
    "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
  }
  SECRET_KEY=get_secret_key()["secret"]
  token = jwt.encode(payload,SECRET_KEY,algorithm="HS256")
  return success("signed in successflly.",{"user_id":new_user,"token":token})