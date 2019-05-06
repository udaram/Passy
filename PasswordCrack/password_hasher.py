import hashlib

def hashing_method():
    passwd_hash=input("Enter password::")
    #print(passwd_hash)
    hash1 = hashlib.md5(passwd_hash.encode('utf-8'))
    print("Your hashed password is:",hash1.hexdigest())

hashing_method()
