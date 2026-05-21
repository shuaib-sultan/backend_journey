class AppError(Exception ):
    def __init__(self,message,status_code,payload=None,log_level="error"):
        super().__init__(message)
        self.message=message
        self.status_code=status_code
        self.payload=payload
        self.log_level=log_level

class NotFoundError(AppError):#when the any resours not found in the systems data.
    def __init__(self,message="Resource not found.", status_code=404,payload=None,log_level="info"):
        super().__init__(message, status_code, payload,log_level)


class ValidationError(AppError):# when the data from user is wrong.
    def __init__(self, message="Validition faild.", status_code=422,payload=None,log_level="warning"):
        super().__init__(message,status_code, payload,log_level)

class AuthenticationError(AppError): #when the authenticaton faild [Wrong user login].
    def __init__(self, message="Authentication failed",status_code=401, payload=None,log_level="warning"):
        super().__init__(message, status_code, payload,log_level)

class PermissionError(AppError):# if the user dosn't admin.
    def __init__(self, message="Permission denied",status_code=403 ,payload=None,log_level="warning"):
        super().__init__(message, status_code, payload,log_level)


class DatabaseError(AppError):# for database server error.
    def __init__(self, message="Database error",status_code=500, payload=None,log_level="error"):
        super().__init__(message, status_code, payload,log_level)

class TooManyRequestsError(AppError):
    def __init__(self, message="Too many request in 1 minutes .",status_code=429, payload=None,log_level="warning"):
        super().__init__(message, status_code, payload,log_level)

class ConflictError(AppError):
    def __init__(self, message="The data already in the system .",status_code=409, payload=None,log_level="warning"):
        super().__init__(message, status_code, payload,log_level)