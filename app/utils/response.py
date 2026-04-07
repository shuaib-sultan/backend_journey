from flask import jsonify
def success(message,data=None,status=200):
  return jsonify({
      "status":"Success",
      "success_message":message,
      "details":data if data is not None else []
    }),status

def error(message,data=None,status=400):
  return jsonify({
      "status":"Error",
      "error_message":message,
      "details":data if data is not None else []
    }),status
