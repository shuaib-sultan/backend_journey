import os
class Config_Db:
  DB_NAME= "users"
  DB_USER= "root"
  DB_HOST="localhost"
  DB_PASSWORD= os.getenv("SECRET_KEY_DB")

def get_db_config():
  return {
    "user":Config_Db.DB_USER,
    "host":Config_Db.DB_HOST,
    "password":Config_Db.DB_PASSWORD,
    "database":Config_Db.DB_NAME
  }

def get_jwt_key():
  return os.getenv("SECRET_KEY_TOKEN")