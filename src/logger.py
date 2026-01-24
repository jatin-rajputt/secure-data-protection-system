from datetime import datetime
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "security.log")

def log_event(message: str):
    """
    Writes security-related events to a log file.
    Ensures log directory exists before writing.
    """
    os.makedirs(LOG_DIR, exist_ok=True)

    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {message}\n")
