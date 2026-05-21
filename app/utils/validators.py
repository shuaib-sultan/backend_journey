import re 
from werkzeug.exceptions import BadRequest
from app.core.errors import ValidationError ,AuthenticationError

def is_valid_email(email):
  pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}$"
  return True if re.match(pattern,email) else False

def check_email(email):
  if not is_valid_email(email) :
    raise ValidationError("Invaild email.")

def check_type(data):
  if  not isinstance(data,str):
    raise ValidationError("Wrong type of data")

def check_pass(password):
  if len(password) < 8 :
    raise ValidationError("The password should be at lest 8 characters .")

def check_empty_field(*data):
  for elemint in data:
    if not elemint :
      raise ValidationError(f"Field {elemint} is empty.")

def empty_request(data):
  if not data :
    raise BadRequest('The json request is empty or bad request.')

def check_synatx(data,requerd):
  if not isinstance(data,dict):
    raise ValidationError("Wrong type of data.")
  for key in requerd:
    if key not in data.keys():
      raise ValidationError(f"The {key} is requerd")

def check_payload(payload,requerd):
  if not payload or not isinstance(payload,dict):
    raise AuthenticationError("Invalid token .")
  for key in requerd:
      if key not in payload.keys():
        raise AuthenticationError("Invalid token .") 

