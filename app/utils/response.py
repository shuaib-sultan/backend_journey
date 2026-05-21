from flask import jsonify

def success(message,status_code,payload=None):
  return jsonify({
      "status":"Success",
      "success_message":message,
      "details":payload if payload is not None else []
    }),status_code

def error(message,status_code,payload=None):
  return jsonify({
      "status":"Error",
      "error_message":message,
      "details": payload if payload is not None else []
    }),status_code
