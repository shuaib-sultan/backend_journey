from app.utils.response import success
from flask import current_app ,g
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
  update_to_admin,
  get_all)
from app.utils.hash import hash_password

def get_users_logic(page,limit):
  try:
    page=int(page);limit=int(limit)
  except ValueError:
    raise ValidationError("Invalid type of argument : [page,limit] should be integer numbers")
  if (limit>100 or (page < 1 or limit < 0)):
    raise ValidationError("Invalid argumentes page[1->100000] limit [10->100]")
  offset=(page-1)*limit
  users=get_users(limit,offset=offset)
  total_users = get_all()[0]["count(user_name)"]
  total_pages = total_users / limit
  has_next_page = page < total_pages
  if not users:
    return success("No users found for this page.",{"page":page,"limit":limit,"total_pages":total_pages,"total_users":total_users,"has_next_page":has_next_page,"data":users},200)
  return success("Users retrieved successfuly .",{"page":page,"limit":limit,"total_pages":total_pages,"total_users":total_users,"has_next_page":has_next_page,"data":users},200)

def get_user_id_logic(id):
  user= get_user_by_id(id)
  if not user:
    raise NotFoundError(f'The id {id} not found .')
  return success(f"User with ID {id} retrieved successfully",{"data":user},200)

def get_user_email_logic(email):
  check_empty(email)
  check_type(email)
  check_email(email)
  result=get_user_by_email(email)
  if not result:
    raise NotFoundError("Email is not found.",404,[])
  return success(f"User with email '{email}' retrieved successfully",{"data":result})

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
  current_app.logger.info(f"The user with id{g.current_user_id} add the user with id {user_id} successfully to the sysetm . ")
  new_user=get_user_by_id(user_id)
  return success(f"The user crated successfully ",{"data":new_user},201)

def update_user_logic_id(id,user_data):
  check_user=get_user_by_id(id)
  if not check_user:
    raise NotFoundError(f"The id {id} is not found soory .",404,[])
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
  current_app.logger.info(f'The user with id {g.current_user_id } update the user {id} successfully .')
  upadated_user=get_user_by_id(id)
  return success(f"The user with id {id} is uapdated successfully.",{"data":upadated_user},201)

def update_user_logic(user_data):
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
  update_user_info(g.current_user_id,user_data)
  current_app.logger.info(f'The user data with id {g.current_user_id } updated successfully .')
  upadated_user=get_user_by_id(id)
  return success(f"The user with id {id} is uapdated successfully.",{"data":upadated_user},201)


def delete_user_logic(id):
  check_user=get_user_by_id(id)
  if not check_user:
    raise NotFoundError(f"The user with id {id} not found.")
  delete_user(id)
  current_app.logger.info(f'The user with id{g.current_user_id } delet the user {id} deleted successfully .')
  return success(f"The user wiht id {id} deleted successfully.",{"data":check_user},200)

def update_to_admin_logic(id):
  user=get_user_by_id(id)
  if not user:
    raise NotFoundError(f'The id {id} not found .')
  if user[0]["role"]=="admin":
    raise ValidationError(f"The user with id {id} is already admin .")
  new_admin=update_to_admin(id)
  current_app.logger.info(f'The user with id {id} upgrade to admin successfully .')
  return success(f"The user with id {id} is admin now.")
