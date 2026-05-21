from app.core.errors import (
  AuthenticationError,
  ConflictError
  )
from app.utiles.validatores import (
  check_email,
  check_empty_field,
  check_pass,
  check_synatx,
  check_type,
  empty_request,
)
from app.utiles.jwt_utiles import ( 
  generate_jwt,
  )
from app.models.user_sql import (
  get_user_by_email,
  add_user,
)
from app.utiles.response import success
from flask import g,current_app
from app.utiles.pass_hashing import hashing,vreify_password

def login_logic(data):
  empty_request(data)
  check_empty_field(data)
  check_synatx(data,["user_email","password"])
  user_name=data["user_name"]
  check_type(user_name)
  user_email=data["user_email"]
  check_type(user_email)
  user_pass=data["password"]
  check_type(user_pass)
  user=get_user_by_email(user_email)
  if not user or not vreify_password(user_pass,user[0]["password"]) :
    raise AuthenticationError("Invalid email or password . ")
  user_role=user[0]["role_id"]
  token=generate_jwt(user[0]["id"],user_role)
  current_app.logger.info(f"The user of id {user[0]["id"]} loged in successfully and take his new valid token." )
  return success("you loged in successfully.",200,{"new_token":token})

def signin_logic(data):
  empty_request(data)
  check_empty_field(data)
  check_synatx(data,["user_name","user_email","password"])
  user_name=data["user_name"]
  check_type(user_name)
  user_email=data["user_email"]
  user=get_user_by_email(user_email)
  check_type(user_email)
  check_email(user_email)
  if user:
    raise ConflictError("The email already in the system . try to login .")
  user_pass=data["password"]
  check_type(user_pass)
  check_pass(user_pass)
  user_pass=hashing(user_pass)
  user=add_user(user_name,user_email,user_pass)
  token=generate_jwt(user[0]["id"],2)
  current_app.logger.info(f"The user of id {user} signup successfully and take his new valid token.")
  return success("you signup successfully.",200,{"new_token":token})

black_token_list=[]

def logout_logic():
  payload= getattr(g,"user_payload")
  if payload["jti"] in black_token_list :
    current_app.logger.warning(f"The user of id {g.user_id} try to logout with invoked token .")
    raise AuthenticationError("The session already exprisson .")
  black_token_list.append(payload["jti"])
  current_app.logger.info(f"The user of id {g.user_id} logedout of the system .")
  return success("you logedout successfully .",200)
