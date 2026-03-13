from app.utils.response import success
from flask import g
from app.core.errors import (
  NotFoundError,
  ValidationError
)
from app.utils.validators import (
  check_syntax,
  check_email,
  check_empty,
  check_type,
  check_password)
from app.models.user_model import(
  get_user_by_email,
  get_user_by_id,
  get_users,
  add_uesr,
  update_user_info,
  delete_user,
  update_to_admin)
from app.utils.hash import hash_password

def get_users_logic():
  users=get_users()
  if len(users)==0:
    return success("The system is empty no user inrolled yet .",users,200)
  return success("Retrieve all user in the system .",users,200)

def get_user_id_logic(id):
  user= get_user_by_id(id)
  return success(f"User with ID {id} retrieved successfully",user,200)

def get_user_email_logic(email):
  check_empty(email)
  check_type(email)
  check_email(email)
  result=get_user_by_email(email)
  if not result:
    raise NotFoundError("Email is not found.",[])
  return success(f"User with email '{email}' retrieved successfully",result)

def add_user_logic(user_data):
  check_syntax(user_data)
  name=user_data['user_name']
  email=user_data['user_email']
  passw=user_data['password']
  check_empty(name,email,passw)
  check_type(name,email,passw)
  check_password(passw)
  check_email(email)
  check_user=get_user_by_email(email)
  if check_user:
    raise ValidationError("The email is already exists",payload=check_user)
  hash_pass=hash_password(passw)
  user_data['password']=hash_pass
  user_id=add_uesr(user_data)
  new_user=get_user_by_id(user_id)
  return success(f"The user crated successfully ",new_user,201)

def update_user_logic(id,user_data):
  check_user=get_user_by_id(id)
  if not check_user:
    raise NotFoundError("The id is not found soory .",[])
  check_syntax(user_data)
  name=user_data['user_name']
  email=user_data['user_email']
  passw=user_data['password']
  check_empty(name,email,passw)
  check_type(name,email,passw)
  check_password(passw)
  check_email(email)
  hash_pass=hash_password(passw)
  user_data['password']=hash_pass
  update_user_info(id,user_data)
  upadated_user=get_user_by_id(id)
  return success(f"The user with id {id} is uapdated successfully.",upadated_user,201)

def delete_user_logic(id):
  check_user=get_user_by_id(id)
  if not check_user:
    raise NotFoundError(f"The user with id {id} not found.")
  delete_user(id)
  return success(f"The user wiht id {id} deleted successfully.",check_user,200)

def update_to_admin_logic(id):
  user=get_user_by_id(id)
  if not user:
    raise NotFoundError(f'The id {id} not found .')
  if user[0]["role"]=="admin":
    raise ValidationError(f"The user with id {id} is already admin .")
  new_admin=update_to_admin(id)
  return success(f"The user with id {id} he/she is admin now.")
