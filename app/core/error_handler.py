"""
Docstring for app.core.error_handler
it's for handel the excption we write in the other file and connect it to the API.
"""
from app.utils.response import error
from app.core.errors import AppError
from flask import current_app
def register_error_handlers(app):
  @app.errorhandler(AppError)
  def handel_app_error(e): #it's catch any raised error you defintion in the errors file .
    current_app.logger.error(e.message)
    return error(e.message,e.payload,e.status_code)
  @app.errorhandler(404)
  def not_found(e):
    current_app.logger.error("Error in the route path.")
    return error("Route not found .",status=404)
  @app.errorhandler(405)
  def method_not_allowed(e):
    current_app.logger.error("The method is not allwod with this route.")
    return error("This methods not allwod",status=405)
  @app.errorhandler(500)
  def internal_error(e):
    current_app.logger.error("Error in the server.")
    return error("Error in the server try later agaien")