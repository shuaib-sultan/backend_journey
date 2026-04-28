import os
from datetime import datetime ,timedelta,timezone
from app.core.errors import TooManyRequestsError
from flask import request


def add_limiter(app):
  @app.before_request
  def rate_limit():
    global ip_list
    ip_list={}
    ip = request.remote_addr
    now=datetime.now(timezone.utc)
    new_list = { key:value for key,value in ip_list.items() if now <= (value["satrt_time"]+ timedelta(seconds=30))}
    if ip not in ip_list:
      ip_list[ip]={
        "count":1,
        "start_time":now
      }
    else:
      ip_list[ip]["count"]+=1
      if ip_list[ip]["count"] >5:
        raise TooManyRequestsError()
    return