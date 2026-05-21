from flask import request,g,current_app
from uuid import uuid4
import time
def register_request_logger(app):
  @app.before_request
  def log_request():
    g.start_time=time.time()
    g.request_id= str(uuid4())
    request_ip = request.remote_addr
    current_app.logger.info(
            f"[REQUEST] id : {getattr(g,'request_id',None)} | method : {request.method} | path : {request.path} "
            f"ip : {request_ip}"
        )
  @app.after_request
  def log_response(response):
        if not getattr(g,"start_time"):
          return response
        duration = round((time.time() - g.start_time) * 1000, 2)
        user_id= getattr(g ,"user_id", None)
        current_app.logger.info(
              f"[RESPONSE] id : {getattr(g,'request_id',None)} | method: {request.method} | path: {request.path} "
              f"| Status: {response.status_code} "
              f"| Time: {duration}ms | User: {user_id}"
          )
        return response