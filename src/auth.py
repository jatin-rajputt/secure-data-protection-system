import json
import os
import hashlib

USER_DB = "users.json"#user database
MAX_ATTEMPTS = 3
_attempts ={}#tracks failed logins (brute force protection)

def hash_password(password: str)->str:
 """ 
 converts plaintext password into irreversible hash.
 """
 return hashlib.sha256(password.encode()).hexdigest()
# Passwords must never be reversible
# Even admin should not know user passwords

def register_user(username: str,password:str):
    users= {}
    if os.path.exists(USER_DB):
        users = json.load(open(USER_DB))
        
    users[username]= {
        "password": hash_password(password),
        "role": "user"
    }
    
    json.dump(users, open(USER_DB,"w"))
    
    
def login_user(username: str, password: str) -> bool:
    global _attempts  # ✅ FIX: tell Python to use global variable

    if username not in _attempts:
        _attempts[username] = 0

    if _attempts[username] >= MAX_ATTEMPTS:
        print("Account locked due to multiple failed attempts.")
        return False

    users = json.load(open(USER_DB))

    if users.get(username, {}).get("password") == hash_password(password):
        _attempts[username] = 0
        return True

    _attempts[username] += 1
    return False




        
    
    