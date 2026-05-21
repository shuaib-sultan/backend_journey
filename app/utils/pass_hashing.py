import bcrypt

def hashing(passowrd):
  salt=bcrypt.gensalt()
  hash_pass=bcrypt.hashpw(passowrd.encode("utf_8"),salt=salt)
  return hash_pass.decode("utf_8")

def vreify_password(input_password,hashed_passowrd):
  return bcrypt.checkpw(input_password.encode("utf_8"),hashed_passowrd.encode("utf_8"))