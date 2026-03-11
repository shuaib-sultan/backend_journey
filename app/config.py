"""
Docstring for app.config:\n
config file for setting of the app and database .\n
It make it easy to change the database server or setting of any model of app .
"""
import os
from dotenv import load_dotenv
load_dotenv()
class Config_db:
  '''
  Class for defintion the db setting.
  '''
  DB_user="root"
  DB_host="localhost"
  DB_name="users"
  DB_password=os.getenv("SECRET_KEY_DB")
  SECRET_KEY=os.getenv("SECRET_KEY")

def get_db_config():
  '''
  Function to get the setting of database server for connection .
  \n\n
  return :
  setting of database as dictionary
  '''
  return {
    "user":Config_db.DB_user,
    "host":Config_db.DB_host,
    "password":Config_db.DB_password,
    "database":Config_db.DB_name,
  }

def get_secret_key():
  return {"secret":Config_db.SECRET_KEY}
