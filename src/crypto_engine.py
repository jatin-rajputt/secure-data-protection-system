import base64 # to convert bainary data into safe text form as pbkdf2 produce raw binary bytes
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes# produce secure cryptography hash algo
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC # it take pass add salt, hash it, repeat hashing as itteration and produce key
from integrity import generate_hash

def _get_salt():
    if not os.path.exists("config/salt.bin"):
        os.makedirs("config", exist_ok=True)
        with open("config/salt.bin", "wb")as f:
            f.write(os.urandom(16))
    return open("config/salt.bin","rb").read()
# Prevents rainbow-table attack
# Makes same password generate different keys

def _derive_key(password: str)-> bytes:
    salt = _get_salt()
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

# Slows brute-force attacks
# Industry standard (NIST)

def encrypt_file(file_path: str, password: str):
    cipher = Fernet(_derive_key(password))
    
    with open (file_path, "rb")as f:
        encrypted_data = cipher.encrypt(f.read())
        
    hash_value = generate_hash(encrypted_data)
        
    os.makedirs("data/encrypted", exist_ok=True)
    output = "data/encrypted/" + os.path.basename(file_path)+ ".enc"
    
    with open(output, "wb")as f:
        f.write(encrypted_data)
        
    with open(output + ".hash", "w")as f:
        f.write(hash_value) 
    return output



def decrypt_file(enc_path: str, password: str):
    # --- Input validation ---
    if enc_path.endswith(".hash"):
        raise ValueError(
            "Invalid input: Please provide the encrypted (.enc) file, not the .hash file."
        )

    if not enc_path.endswith(".enc"):
        raise ValueError(
            "Invalid file type: Only .enc files can be decrypted."
        )

    hash_path = enc_path + ".hash"

    if not os.path.exists(hash_path):
        raise ValueError(
            "Integrity metadata (.hash) file missing. Decryption blocked."
        )

    # --- Key derivation ---
    cipher = Fernet(_derive_key(password))

    # --- Read encrypted data ---
    with open(enc_path, "rb") as f:
        encrypted_data = f.read()

    # --- Read and normalize stored hash ---
    with open(hash_path, "r") as f:
        stored_hash = f.read().strip()

    # --- Integrity verification ---
    if generate_hash(encrypted_data) != stored_hash:
        raise ValueError(
            "Integrity check failed! File may be tampered."
        )

    # --- Decrypt only if integrity is valid ---
    decrypted_data = cipher.decrypt(encrypted_data)

    os.makedirs("data/decrypted", exist_ok=True)
    output = "data/decrypted/" + os.path.basename(enc_path).replace(".enc", "")

    with open(output, "wb") as f:
        f.write(decrypted_data)

    return output
