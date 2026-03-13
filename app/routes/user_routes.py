from flask import Blueprint ,request,g
from app.core.auth_middleware import require_auth,auth_admin
from app.services.user_service import( 
get_user_email_logic,
get_users_logic,
get_user_id_logic,
add_user_logic,
update_user_logic,
delete_user_logic,
update_to_admin_logic)
from app.utils.response import success

user_bp= Blueprint("users",__name__)
@user_bp.route("/")
def home ():
  return ""

@user_bp.route("/users",methods=["GET"])
@require_auth
def retrieve_users():
  return get_users_logic()

@user_bp.route("/user/byint/<int:id>",methods=["GET"])
@require_auth
def retrieve_user_id(id):
  return get_user_id_logic(id)

@user_bp.route("/user/byemail/<string:email>",methods=["GET"])
@require_auth
def retrieve_user_email(email):
  return get_user_email_logic(email)

@user_bp.route("/user/add",methods=["POST"])
@require_auth
@auth_admin
def creat_user():
  new_user= request.get_json()
  return add_user_logic(new_user)

@user_bp.route("/user/<int:id>",methods=["PUT"])
@require_auth
def update_user(id):
  new_user=request.get_json()
  return update_user_logic(id,new_user)

@user_bp.route("/user/<int:id>",methods=["DELETE"])
@require_auth
def remove_user(id):
  return delete_user_logic(id)

@user_bp.route("/add/admin/<int:id>",methods=["PUT"])
@require_auth
@auth_admin
def add_admin(id):
  return update_to_admin_logic(id)
