import os
from flask import request,g
from app.services.rate_limiter import Ratelimiter
from app.core.errors import TooManyRequestsError
from functools import wraps
ipLimiter = Ratelimiter(int(os.getenv("MAX_REQUESTS",5)),int(os.getenv("WINDOW_SECONDS",60)))

def rate_limit_IP():
  allwoed=ipLimiter.is_allowed(request.remote_addr)
  if not allwoed:
    raise TooManyRequestsError()
  return

idLimiter=Ratelimiter(int(os.getenv("MAX_REQUESTS",5)),int(os.getenv("WINDOW_SECONDS",60)))

def rate_limit_id_midelware(fun):
  @wraps (fun)
  def wrapper(*args,**kargs):
    allowed=ipLimiter.is_allowed(g.user_id)
    if not allowed:
      raise TooManyRequestsError
    return fun(*args,**kargs)
  return wrapper

def limit_rate(app):
  @app.before_request
  def rate_limiting(*args,**kargs):
    if request.path.startswith("/apidocs") or request.path.startswith("/flasgger_static"):
        return
    rate_limit_IP()