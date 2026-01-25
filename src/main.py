from auth import register_user, login_user
from crypto_engine import encrypt_file, decrypt_file
from logger import log_event

def menu():
    print("\n1. Register")
    print("\n2. Login")
    print("\n3. Exit")
    
def secure_actions(username, password):
    print("\n1.Encrypted File")
    print("\n2.Decrypted File")
    
    choice = input("Choose option: ")
    
    if choice =="1":
        path = input("Enter file path: ")
        output = encrypt_file(username, path, password)
        log_event(f"{username} encrypted file: {path}")
        print("Encrypted ->", output)
        
    elif choice =="2":
        path = input("Enter encrypted file path: ")
        output = decrypt_file(username, path, password)
        log_event(f"{username} decrypted file: {path}")
        print("Decrypted ->", output)
        
        
print("Secure Data Protection System")

while True:
    menu()
    choice = input("Select option: ")

    if choice == "1":
        register_user(input("Username: "),input("Password: "))
        log_event("New user registered")
        
    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")

        if login_user(username, password):
            log_event(f"Login success: {username}")
            secure_actions(username, password)
        else:
            log_event(f"Login failed: {username}")
            
    elif choice == "3":
        break