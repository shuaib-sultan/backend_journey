"""
Docstring for app.core.error
it's for make your own error that we will use in error handelr. 
"""
class AppError(Exception):
  def __init__(self,message,status_code,payload=None) :
    super().__init__(message) # to make all the Exception enhirt the excption class and decorate it by add the code_status and message.
    self.message=message
    self.status_code=status_code
    self.payload=payload

class NotFoundError(AppError):#when the some thing not found 
  def __init__(self,message="Resource not found.", status_code=404,payload=None):
    super().__init__(message, status_code, payload)

class ValidationError(AppError):# when the data from user is wrong.
  def __init__(self, message="Validition faild.", status_code=400,payload=None):
    super().__init__(message,status_code, payload)

class AuthenticationError(AppError):
    def __init__(self, message="Authentication failed",status_code=401, payload=None):
        super().__init__(message, status_code, payload)


class PermissionError(AppError):
    def __init__(self, message="Permission denied",status_code=403 ,payload=None):
        super().__init__(message, status_code, payload)


class DatabaseError(AppError):# for sql error
    def __init__(self, message="Database error",status_code=500, payload=None):
        super().__init__(message, status_code, payload)

class TooManyRequestsError(AppError):
    def __init__(self, message="TooManyRequests eroor",status_code=500, payload=None):
       super().__init__(message,status_code, payload)
