import re
from app.core.errors import ValidationError,NotFoundError
def is_email(email):
  pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}$"
  return True if re.match(pattern,email) else False

def check_email(email):
  if not is_email(email):
    raise ValidationError("The email is invalid.",600,{
        "Expect":{ 
          "user_name":"name(string type)[ NOT EMPTY ]",
          "user_email":"user_name@example.com (string type)[ NOT EMPTY ]",
          "password":"user_password (string)[ NOT EMPTY ][at lest 8 characters]"}})
  return True

def check_syntax(data,requird=["user_email","user_name","password"]):
  if not isinstance(data,dict):
    raise ValidationError("Invalid input format, expected JSON object",600,{
        "Expect":{ 
          "user_name":"name(string type)[ NOT EMPTY ]",
          "user_email":"user_name@example.com (string type)[ NOT EMPTY ]",
          "password":"user_password (string)[ NOT EMPTY ][at lest 8 characters]"}})
  for key in requird:
    if key not in data.keys():
      raise NotFoundError(f"The field {key} is messing",600,{
        "Expect":{ 
          "user_name":"name(string type)[ NOT EMPTY ]",
          "user_email":"user_name@example.com (string type)[ NOT EMPTY ]",
          "password":"user_password (string)[ NOT EMPTY ][at lest 8 characters]"}})
  return True

def check_type(*values):
  for value in values:
    if not isinstance(value,str):
      raise ValidationError("Invalid syntax",600,{
        "Expect":{ 
          "user_name":"name(string type)[ NOT EMPTY ]",
          "user_email":"user_name@example.com (string type)[ NOT EMPTY ]",
          "password":"user_password (string)[ NOT EMPTY ][at lest 8 characters]"}})
  return True

def check_password(passw):
  if len(passw)<8 :
    raise ValidationError("Password must be at least 8 characters long")
  return True

def check_empty(*values,message="Empty field is not allowed"):
  for value in values:
    if not value.strip():
      raise ValidationError(message)
  return True