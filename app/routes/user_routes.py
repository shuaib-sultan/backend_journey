from flask import Blueprint ,request
from app.core.auth_middleware import require_auth,auth_admin
from app.services.user_service import( 
get_user_email_logic,
get_users_logic,
get_user_id_logic,
add_user_logic,
update_user_logic_id,
delete_user_logic,
update_to_admin_logic,
update_user_logic)
from app.utils.response import success

user_bp= Blueprint("users",__name__)
@user_bp.route("/")
def home ():
  return ""

@user_bp.route("/users",methods=["GET"])
@require_auth
def retrieve_users():
  pag=request.args.get("page",1)
  limit=request.args.get("limit",10)
  return get_users_logic(pag,limit)

@user_bp.route("/user/id/<int:id>",methods=["GET"])
@require_auth
def retrieve_user_id(id):
  return get_user_id_logic(id)

@user_bp.route("/user/email/<string:email>",methods=["GET"])
@require_auth
def retrieve_user_email(email):
  return get_user_email_logic(email)

@user_bp.route("/user/add",methods=["POST"])
@require_auth
@auth_admin
def creat_user():
  new_user= request.get_json()
  return add_user_logic(new_user)

@user_bp.route("/user/update/<int:id>",methods=["PUT"])
@require_auth
@auth_admin
def update_user_by_id(id):
  new_user=request.get_json()
  return update_user_logic_id(id,new_user)

@user_bp.route("/user/update",methods=["POT"])
@require_auth
def update_user():
  updated_info=request.get_json()
  return update_user_logic(updated_info)

@user_bp.route("/user/<int:id>",methods=["DELETE"])
@require_auth
def remove_user(id):
  return delete_user_logic(id)

@user_bp.route("/add/admin/<int:id>",methods=["PUT"])
@require_auth
@auth_admin
def add_admin(id):
  return update_to_admin_logic(id)
