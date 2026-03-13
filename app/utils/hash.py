import bcrypt
def hash_password(plain_password):
    #the bcrypt dont take and return else the Bytes so we do encode() and use the UTF_8 to make sure the user mube will use any languegh 
    # utf_8 to convert byte to string and the reverse of that.
    salt = bcrypt.gensalt() # to ginerate some number and add it to the password which mean no two pass has the same hashing.
    hashed = bcrypt.hashpw(plain_password.encode("utf-8"), salt)
    return hashed.decode("utf-8")

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw( #this is a fun in bcrypt to check if two password is equal . take the bytes just.
        plain_password.encode("utf-8"), # encude cuse we get the password as string and we need to convert it to bytes
        hashed_password.encode("utf-8")
    )