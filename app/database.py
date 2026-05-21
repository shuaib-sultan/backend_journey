import mysql.connector
from app.config import get_db_config
from app.core.errors import DatabaseError,ConflictError
from mysql.connector import pooling
from flask import current_app
def create_pool():
      return pooling.MySQLConnectionPool(
        pool_size=10,
        pool_name="DB_pool",
        **get_db_config()
      )

pool = create_pool()

def query(sql,params=None,fetch=True):
  db=None
  cursor=None
  db= pool.get_connection()
  cursor= db.cursor(dictionary=True)
  try:
    cursor.execute(sql,params or ())
    if fetch:
      result=cursor.fetchall()
      return result
    else:
      db.commit()
      result=cursor.lastrowid
      return result
  except mysql.connector.errors.PoolError as e :
    raise DatabaseError("The server is full now try leater .")
  except mysql.connector.Error as e:
    current_app.logger.error(f"DB_ERROR | sql= {sql} | parameter={params} | ")
    if e.errno ==1062:
      raise ConflictError(str(e))
    raise DatabaseError(str(e))
  finally:
    if cursor:
      cursor.close()
    if db:
      db.close()