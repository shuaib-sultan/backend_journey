from app.database import query
def get_users(limit,offset,filters,params):
  sql="select * from user_info "
  if filters:
    sql+=" where "+ " and ".join(filters)
  sql += " order by id LIMIT %s OFFSET %s ;"
  # result=query(sql,(*params,limit,offset)) if filters else query(sql,(limit,offset))
  result = query(sql, (*params, limit, offset))
  return result

def count_users():
    sql="select count(user_name) as total from user_info "
    result=query(sql)
    return result

def get_user(id):
  sql="select * from user_info where id = %s "
  result=query(sql,(id,))
  return result

def get_user_by_email(email):
  sql="select * from user_info where user_email = %s "
  result=query(sql,(email,))
  return result

def add_user(user_name,user_email,user_pass):
  sql="insert into user_info(user_name,user_email,password)\
      values(%s,%s,%s);"
  result=query(sql,(user_name,user_email,user_pass),fetch=False)
  return result

def update_user_byId(user_name,user_email,user_pass,id):
  sql="update user_info set user_name = %s ,user_email = %s ,password = %s where id = %s ;"
  query(sql,(user_name,user_email,user_pass,id),False)
  return id

def update_user(user_name,user_email,user_pass):
  sql="update user_info set user_name = %s ,user_email = %s ,password = %s where id = %s ; "
  query(sql,(user_name,user_email,user_pass,id),False)

def delet_user(id):
  sql="deleteform user_info where id = %s ; "
  query(sql,(id,),False)
  return id

def update_to_admin(id):
  sql="update user_info set role_id = 1 where id = %s ;"
  result=query(sql,(id,),False)
  return result
