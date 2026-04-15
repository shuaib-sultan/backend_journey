import mysql.connector
from app.config import get_db_config
from app.core.errors import DatabaseError
from mysql.connector import pooling
db_config=get_db_config()
pool= pooling.MySQLConnectionPool(
  pool_size=5,
  pool_name="DB_pool",
  **db_config
)
def query(sql,params=(),fech=True):
  db=pool.get_connection()
  cursor=db.cursor(dictionary=True)
  try:
    cursor.execute(sql,params or ())
    if fech:
      result=cursor.fetchall()
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