from flask import Blueprint ,request
from app.services.user_service import( 
get_user_email_logic,
get_users_logic,
get_user_id_logic,
add_user_logic,
update_user_logic,
delete_user_logic)

user_bp= Blueprint("users",__name__)
@user_bp.route("/")
def home ():
  return ""

@user_bp.route("/users",methods=["GET"])
def retrieve_users():
  return get_users_logic()

@user_bp.route("/user/<int:id>",methods=["GET"])
def retrieve_user_id(id):
  return get_user_id_logic(id)

@user_bp.route("/user/<string:email>",methods=["GET"])
def retrieve_user_email(email):
  return get_user_email_logic(email)

@user_bp.route("/user/",methods=["POST"])
def creat_user():
  new_user= request.get_json()
  return add_user_logic(new_user)

@user_bp.route("/user/<int:id>",methods=["PUT"])
def update_user(id):
  new_user=request.get_json()
  return update_user_logic(id,new_user)

@user_bp.route("/user/<int:id>",methods=["DELETE"])
def remove_user(id):
  return delete_user_logic(id)