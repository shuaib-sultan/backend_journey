from flask import Blueprint,request
from app.services.auth_service import (login_logic,logout_logic,signin_logic)
auth_bp=Blueprint('auth',__name__)

@auth_bp.route("/login",methods=["POST"])
def login():
  data=request.get_json(silent=True)
  return login_logic(data)

@auth_bp.route("/sigup",methods=["POST"])
def sigup():
  data=request.get_json(silent=True)
  return signin_logic(data)

@auth_bp.route("/logout",methods=["POST"])
def logout():
  return logout_logic()


