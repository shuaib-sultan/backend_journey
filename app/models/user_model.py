'''
Docstring for app.models.user_model
It's file for sql functuin for CRUD actions.
'''
from app.database import query
def get_users(limit,offset,filters,params):
  sql= "select * from user_info "
  if filters :
    sql+=" where "+ " and ".join(filters)
  sql+=" order by id limit %s offset %s;"
  result=query(sql,(*params,limit , offset))
  return result

def get_all():
  sql="select count(user_name) as total from user_info "
  result=query(sql)
  return result

def get_user_by_id(user_id):
  sql="select * from user_info where id=%s;"
  result=query(sql,(user_id,))
  return result

def get_user_by_email(user_email):
  sql="select * from user_info where user_email=%s;"
  result=query(sql,(user_email,))
  return result

def add_uesr(user_data):
  sql="insert into user_info(user_name,user_email,password) values(%s,%s,%s);"
  result=query(sql,(user_data["user_name"],user_data["user_email"],user_data["password"]),False)
  return result

def update_user_info(id,user_data):
  sql="update user_info set user_name=%s,user_email=%s,password=%s where id=%s ;"
  result=query(sql,(user_data["user_name"],user_data["user_email"],user_data["password"],id),False)
  return result

def delete_user(id):
  sql="delete from user_info where id =%s;"
  result=query(sql,(id,),False)
  return result

def update_to_admin(id):
  sql="update user_info set role = 'admin' where id = %s ;"
  result=query(sql,(id,))
  return result
