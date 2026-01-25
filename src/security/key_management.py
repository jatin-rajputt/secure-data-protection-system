import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

USER_SALT_DIR = "config/user_salts"

def get_user_salt(username: str)->bytes:
    """
    Each user get a unique salt.
    Prevents rainbow-table and cross-user attacks.
    """
    
    os.makedirs(USER_SALT_DIR, exist_ok=True)
    salt_path = os.path.join(USER_SALT_DIR,f"{username}.bin")
    
    if not os.path.exists(salt_path):
        with open (salt_path,"wb") as f:
            f.write(os.urandom(16))
            
    with open(salt_path, "rb")as f:
        return f.read()
    
    
def derive_user_key(username: str, password: str)-> bytes:
    """
    Derives a strong encryption key using PBKDF2>
    
    """
    
    salt = get_user_salt(username)
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=200_000,
    )
    
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))