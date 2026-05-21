from flask import Blueprint,request
from app.core.rate_limit import rate_limit_id_midelware
from app.core.auth_middleware import auth_required ,role_required
from app.services.user_service import(
                                       add_user_logic,
                                       get_users_logic,
                                       delet_user_logic,
                                       update_user_logic,
                                       update_admin_logic,
                                       update_user_buId_logic,
                                       get_user_byEmail_logic,
                                       get_user_byId_logic,
                                       )
users_bp=Blueprint("users",__name__,url_prefix="/users")

@users_bp.route("/users",methods=["GET"])
@auth_required
@rate_limit_id_midelware
def ritrive_users():
  page=int(request.args.get("page",1))
  limit=int(request.args.get("limit",10))
  allwoed_filters=["role"]
  filtters=[]
  params=[]
  for arg , value in request.args.items():
    if arg.strip() in allwoed_filters:
      filtters.append(f"{arg} =  %s  ")
      params.append(value.strip())
  return get_users_logic(page,limit,filtters,params)

@users_bp.route("/addUser",methods=["POST"])
@auth_required
@rate_limit_id_midelware
@role_required("admin")
def add_user():
  user_data=request.get_json(silent=True)
  return add_user_logic(user_data)

@users_bp.route("/update",methods=["PUT"])
@auth_required
@rate_limit_id_midelware
def update_user():
  data=request.get_json(silent=True)
  return update_user_logic(data)

@users_bp.route("/updateUser/<int:id>",methods=["PUT"])# for admin just.
@auth_required
@rate_limit_id_midelware
@role_required("admin")
def update_user_by_id(id):
  data=request.get_json(silent=True)
  return update_user_buId_logic(id,data)

@users_bp.route("deleteUser/<int:id>",methods=["DELETE"])#for admin just .
@auth_required
@rate_limit_id_midelware
@role_required("admin")
def delet_user(id):
  return delet_user_logic(id)

@users_bp.route("/userById/<int:id>",methods=["GET"])
@auth_required
@rate_limit_id_midelware

def get_by_id(id):
  return get_user_byId_logic(id)


@users_bp.route("/userByEmail/<string:email>",methods=["GET"])
@auth_required
@rate_limit_id_midelware
def get_by_email(email):
  return get_user_byEmail_logic(email)

@users_bp.route("/addAdmin/<int:id>",methods=["PUT"])
@auth_required
@rate_limit_id_midelware
@role_required("admin")
def to_admin(id):
  return update_admin_logic(id)
