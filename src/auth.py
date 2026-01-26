import json
import os
import hashlib
from logger import log_event
from security.brute_force import (
    is_account_locked,
    record_failed_attempt,
    reset_attempts,
    get_remaining_lock_time
)

# User database location
USER_DB = "config/users.json"


# -------------------------
# Password Hashing
# -------------------------
def hash_password(password: str) -> str:
    """
    Converts plaintext password into irreversible hash.
    """
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password: str, stored_hash: str) -> bool:
    """
    Verifies user-entered password against stored hash.
    """
    return hash_password(password) == stored_hash


# -------------------------
# User Storage
# -------------------------
def load_users() -> dict:
    if not os.path.exists(USER_DB):
        return {}

    with open(USER_DB, "r") as f:
        return json.load(f)


def save_users(users: dict):
    os.makedirs("config", exist_ok=True)
    with open(USER_DB, "w") as f:
        json.dump(users, f, indent=4)


# -------------------------
# Registration
# -------------------------
def register_user(username: str, password: str):
    users = load_users()

    if username in users:
        print("User already exists.")
        return False

    users[username] = {
        "password": hash_password(password),
        "role": "user"
    }

    save_users(users)
    log_event(f"User registered: {username}")
    return True


# -------------------------
# Login (with Brute Force Protection)
# -------------------------
def login_user(username: str, password: str) -> bool:
    # Step 1: Check lock status
    if is_account_locked(username):
        remaining = get_remaining_lock_time(username)
        log_event(f"LOCKED login attempt for '{username}' ({remaining}s remaining)")
        print(f"Account locked. Try again in {remaining} seconds.")
        return False

    users = load_users()

    if username not in users:
        record_failed_attempt(username)
        log_event(f"FAILED login: invalid user '{username}'")
        print("Invalid credentials.")
        return False

    stored_hash = users[username]["password"]

    if not verify_password(password, stored_hash):
        record_failed_attempt(username)
        log_event(f"FAILED login: wrong password for '{username}'")
        print("Invalid credentials.")
        return False

    # Step 2: Successful login
    reset_attempts(username)
    log_event(f"SUCCESS login for '{username}'")
    return True
