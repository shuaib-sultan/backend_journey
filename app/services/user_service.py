from app.utils.response import success
from flask import g,current_app
from app.core.errors import (
  ValidationError,
  NotFoundError,
  ConflictError
)
from app.models.user_sql import (
  get_user,
  get_user_by_email,
  get_users,
  count_users,
  add_user,
  update_to_admin,
  update_user,
  delet_user,
)
from app.utils.validators import (
  check_email,
  check_empty_field,
  check_pass,
  check_synatx,
  check_type,
  empty_request)

def get_users_logic(page,limit,filters,params):
  if not isinstance(page,int):
    raise ValidationError("The page parameters muste be a number.")
  if not isinstance(limit,int):
    raise ValidationError("The limit of users parameters muste be a number.")
  if limit < 5 :
    raise ValidationError("Invaild number of limit [ limit >= 5 ].")
  if page < 1:
    raise ValidationError("Invalid number of page [ page >= 1 ].")
  if filters :
    for param in params :
      if not isinstance(param,str):
        raise ValidationError("The parameters of filters must be string .")
  offset=(page-1)*limit
  total_users= count_users()[0]["total"]
  from math import ceil
  total_pages= ceil(total_users/limit)
  users=get_users(limit,offset,filters,params)
  current_app.logger.info("The user ritrive the users successfully.")
  return success("The users retrive successfully.",200,{
    "page":page,
    "limit":limit,
    "total_pages":total_pages,
    "total_users":total_users,
    "data":users
  })

def add_user_logic(data):
  empty_request(data)
  check_empty_field(data)
  check_synatx(data,["user_name","user_email","password"])
  user_name=data["user_name"]
  check_type(user_name)
  user_email=data["user_email"]
  check_type(user_email)
  check_email(user_email)
  user_pass=data["password"]
  check_type(user_pass)
  if get_user_by_email(user_email):
    raise ConflictError("The user already on the system .")
  check_pass(user_pass)
  new_user_id=add_user(user_name,user_email,user_pass)
  current_app.logger.info(f"The adimn of id {g.user_id} add user of id {new_user_id} to the system successfully .")
  return success("The user added successfully .",201,{'new_user_id':new_user_id})

def delet_user_logic(id):
  user=get_user(id)
  if not user:
    raise NotFoundError(f"The user with id {id} is not found .")
  delet_user(id)
  current_app.logger.info(f"The admin of id {g.user_id} delete the user of id {id} successfully.")
  return success (f"The user of id {id} deleted successfully.",200)

def update_user_logic(data):
  empty_request(data)
  check_empty_field(data)
  check_synatx(data,["user_name","user_email","password"])
  user_name=data["user_name"]
  check_type(user_name)
  user_email=data["user_email"]
  check_type(user_email)
  check_email(user_email)
  user_pass=data["password"]
  check_type(user_pass)
  check_pass(user_pass)
  update_user(user_name,user_email,user_pass)
  current_app.logger.info(f"The user of id {g.user_id} update his information .")
  return success ("The information updated successfully .",200,)

def update_user_buId_logic(id,data):
  empty_request(data)
  user=get_user(id)
  if not user:
    raise NotFoundError(f"The user of id {id} not found .")
  check_empty_field(data)
  check_synatx(data,["user_name","user_email","password"])
  user_name=data["user_name"]
  check_type(user_name)
  user_email=data["user_email"]
  check_type(user_email)
  check_email(user_email)
  user_pass=data["password"]
  check_type(user_pass)
  check_pass(user_pass)
  update_user(user_name,user_email,user_pass)
  current_app.logger.info(f"The admin of id {g.user_id} update the users information .")
  return success ("The information updated successfully .",200,)

def update_admin_logic(id):
  user=get_user(id)
  if not user:
      raise NotFoundError(f"The user of id {id} not found .")
  update_to_admin(id)
  current_app.logger.info(f'The admin of id {g.user_id} update the ueser of id {id} to adim')
  return success(f'The user of id {id} update to admi successfully.',200)

def get_user_byEmail_logic(email):
  check_empty_field(email)
  check_type(email)
  check_email(email)
  user=get_user_by_email(email)
  if not user:
    raise NotFoundError("The email not found .")
  return success(f"The user of email '{email} 'retrived successfully.",200,{"data":user})

def get_user_byId_logic(id):
  if not isinstance(id,int):
    raise ValidationError("The id must be a integer number.")
  user=get_user(id)
  if not user:
    raise NotFoundError(f"The user of id {id} not found in the system .")
  return success(f"The user of id {id} retrived successfully.",200,{"data":user})