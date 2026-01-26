import time
from typing import Dict


MAX_ATTEMPTS = 5
LOCK_TIME =300 

_attempts: Dict[str, dict] = {}

def is_account_locked(username):

    user = _attempts.get(username)
    if not user:
        return False

    lock_until = user.get("lock_until", 0)

    # Still locked
    if time.time() < lock_until:
        return True

    # Lock expired → reset ONLY if it was locked before
    if lock_until > 0:
        reset_attempts(username)

    return False

def record_failed_attempt(username: str):
    #Records a failed login attempt. Lock accont if threshold exceeded.

    user = _attempts.setdefault(username, {
        "failures":0,
        "lock_until":0
    }) 
    
    user["failures"]+=1
    
    
    if user["failures"]>= MAX_ATTEMPTS:
        user["lock_until"] = time.time() + LOCK_TIME
        
        
        
def reset_attempts(username: str):
    #clear brute-force counters after successful login.
    
    if username in _attempts:
        del _attempts[username]
        
        
def get_remaining_lock_time(username: str)-> int:
    #returning remaing lock time in seconds.
    
    user = _attempts.get(username)
    if not user:
        return 0
    remaining = int(user["lock_until"] - time.time())
    return max(0, remaining)