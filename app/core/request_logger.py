import time
from flask import request, g, current_app
def register_request_logger(app):
    @app.before_request
    def log_request():
        g.start_time = time.time()
        user_id = getattr(g, "current_user_id", None)
        current_app.logger.info(
            f"[REQUEST] {request.method} {request.path} | Body: {request.get_json(silent=True)}"
        )
    @app.after_request
    def log_response(response):
        duration = round((time.time() - g.start_time) * 1000, 2)
        current_app.logger.info(
            f"[RESPONSE] {request.method} {request.path}| User: some bich:O "
            f"| Status: {response.status_code} "
            f"| Time: {duration}ms "
        )
        return response
