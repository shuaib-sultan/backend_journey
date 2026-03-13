from flask import Flask
def create_app():
  app= Flask(__name__)
  from app.routes.user_routes import user_bp
  app.register_blueprint(user_bp)
  from app.routes.auth_routes import auth_bp
  app.register_blueprint(auth_bp)
  from app.core.error_handler import register_error_handlers
  register_error_handlers(app)
  return app
