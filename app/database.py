import mysql.connector
from app.config import get_db_config
from app.core.errors import DatabaseError
def connect_db():
  db_config=get_db_config()
  db=mysql.connector.connect(**db_config)
  return db
def query(sql,params=(),fech=True):
  db=connect_db()
  cursor=db.cursor(dictionary=True)
  try:
    cursor.execute(sql,params or ())
    if fech:
      result=cursor.fetchall()
      print(result)
      return result
    else:
      db.commit()
      result=cursor.lastrowid
      return result
  except mysql.connector.Error as e:
    raise DatabaseError(str(e))
  finally:
    cursor.close()
    db.close()
