import hashlib

def hashing_method(passwd_hash):
    hash1 = hashlib.md5(passwd_hash.encode('utf-8'))
    
    print("Your hashed password is:",hash1.hexdigest())

def main():
    passwd_hash=input("Enter your password:")
    hashing_method(passwd_hash)

if __name__=="__main__":
    main()
    

