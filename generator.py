import time
from datetime import datetime

LOG_FILE = "logs/raw_logs.txt"

def simulate_logs():
    sample_events = [
        "LOGIN - User admin from 192.168.1.5",
        "LOGIN_FAIL - User guest from 10.0.0.1",
        "FILE_ACCESS - /etc/passwd by root",
        "LOGIN - User elvis from 172.16.0.8",
        "LOGIN_FAIL - User hacker from 192.168.0.99"
    ]

    while True:
        log = f"{datetime.now()} - {sample_events[datetime.now().second % len(sample_events)]}"
        with open(LOG_FILE, "a") as f:
            f.write(log + "\n")
        time.sleep(5)
