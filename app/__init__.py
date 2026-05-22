def creat_app():
  from dotenv import load_dotenv
  load_dotenv()
  from flask import Flask
  app=Flask(__name__)
  from flasgger import Swagger
  open_api_template="documentation/app_documentation.yaml"
  Swagger(app,template_file=open_api_template)
  from app.routes.users_blueprint import users_bp
  app.register_blueprint(users_bp)
  from app.routes.auth_bleuprint import auth_bp
  app.register_blueprint(auth_bp)
  from app.core.logger_system import creat_logger_system
  app.logger=creat_logger_system()
  from app.core.logger_request import register_request_logger
  register_request_logger(app)
  from app.core.rate_limit import limit_rate
  limit_rate(app)
  from app.core.error_handler import register_error_handlers
  register_error_handlers(app)
  return app
