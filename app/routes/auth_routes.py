from flask import Blueprint, request
from app.services.auth_service import login_logic,sign_up_logic

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    user_data = request.get_json()
    return login_logic(user_data)

@auth_bp.route("/signup",methods=["POST"])
def signup():
    data=request.get_json()
    return sign_up_logic(data)