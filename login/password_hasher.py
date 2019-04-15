import hashlib

def hashing_method(passwd_hash):
    hash1 = hashlib.md5(passwd_hash.encode('utf-8'))
    return hash1.hexdigest()
    #print("Your hashed password is:",hash1.hexdigest())



