import hashlib
import pandas as pd
import numpy as np

def dictionary_attack(password_hash):
    #dictionary = ['letmein','password','12345','football']
    dictionary=pd.read_csv("password.csv")
    dictionary=np.array(dictionary)
    #dictionary=dictionary[:,[0]]
    
    

    password_found=False
    print(dictionary.size)
    for dictionary_value in dictionary:
       #print(dictionary_value[0])
        hashed_value =(hashlib.md5(str(dictionary_value[0]).encode('utf-8'))).hexdigest()
        if hashed_value == password_hash:
            password_found=True
            recovered_password=dictionary_value[0]
            
            
    if password_found==True:
        print("Found match for hashed value \n",password_hash)
        print("password recovered:",recovered_password )

    else:
        print("password was not found")

def main():
    password_hash=input("Enter hashed value:")
    dictionary_attack(password_hash)

if __name__=="__main__":
    main()


