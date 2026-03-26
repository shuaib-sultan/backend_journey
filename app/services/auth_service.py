import jwt
from datetime import datetime,timezone,timedelta
from flask import current_app
from app.utils.validators import (check_email,check_empty,check_password,check_type,check_syntax)
from app.models.user_model import(get_user_by_email,get_user_by_id,add_uesr)
from app.core.errors import ValidationError
from app.utils.response import success
from app.config import get_secret_key
from app.utils.hash import verify_password,hash_password

def login_logic(user_data):
  email=user_data.get("user_email")
  password=user_data.get("password")
  check_empty(email,password,"Email and password are required.")
  check_password(password)
  user=get_user_by_email(email)
  if not user:
    raise ValidationError("Emial is not valid you should signup ")
  plain_pass=password
  hash_pass=user[0]["password"]
  if not verify_password(plain_pass,hash_pass):
    raise ValidationError("Wrong password")
  current_app.logger.info(f"The user {user[0]["user_name"]} with id {user[0]["id"]} loged in .")
  payload={
    "user_id":user[0]["id"],
    "role":user[0]["role"],
    "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
}
  SECRET_KEY=get_secret_key()["secret"]
  token = jwt.encode(payload,SECRET_KEY,algorithm="HS256")
  current_app.logger.info(f"The user {user[0]["id"]} take his token successfully")
  return success("Logedin successfully.",{"token":token})

def sign_up_logic(user_data):
  check_type(user_data["user_name"],user_data["user_email"],user_data["password"])
  check_syntax(user_data)
  check_empty(user_data["user_name"],user_data["user_email"],user_data["password"])
  email=user_data["user_email"]
  check_email(email)
  password=user_data["password"]
  check_password(password)
  user=get_user_by_email(email)
  if user:
    raise ValidationError("This email is already in the system log in to get your new token .")
  hash_pass=hash_password(password)
  user_data["password"]=hash_pass
  new_user=add_uesr(user_data)
  current_app.logger.info(f"The user with id {new_user} sing in sucessfully")
  payload={
    "user_id":new_user,
    "role":"user",
    "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
  }
  SECRET_KEY=get_secret_key()["secret"]
  token = jwt.encode(payload,SECRET_KEY,algorithm="HS256")
  current_app.logger.info(f"The user with id {new_user} take his token successfully.")
  return success("signed in successflly.",{"user_id":new_user,"token":token})