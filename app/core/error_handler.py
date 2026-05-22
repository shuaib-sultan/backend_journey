from flask import current_app ,request
from app.core.errors import AppError
from app.utils.response import error
from werkzeug.exceptions import BadRequest
# import traceback

def register_error_handlers(app):
  @app.errorhandler(AppError)
  def app_error_handler(e):
    allowed_levels = {"debug", "info", "warning", "error", "critical"}
    level = e.log_level if e.log_level in allowed_levels else "error"
    log_fun = getattr(current_app.logger, level)
    log_fun(e.message)
    return error(e.message,e.status_code,e.payload)

  @app.errorhandler(BadRequest)
  def bad_request(e):
    current_app.logger.warning(str(e))
    return error("Invalid request payload",400)

  @app.errorhandler(404)
  def notfound(e):
    current_app.logger.warning(
    f"{str(e)} | path={request.path} | method={request.method}"
)
    return error(f"The {request.path} not found .",status_code=404)
  
  @app.errorhandler(405)
  def wrong_method(e):
    current_app.logger.warning(
    f"{str(e)} | path={request.path} | method={request.method}"
)
    return error(f"Method {request.method} not allwoed .",status_code=405)
  
  @app.errorhandler(500)
  def server_error(e):
    current_app.logger.exception(e)
    return error("Server Error",status_code=500)
  
  @app.errorhandler(Exception)
  def Exeption_handler(e):
    current_app.logger.exception(e)
    return error("Internal server error",500)
