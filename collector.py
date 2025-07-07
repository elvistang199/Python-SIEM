import os
from datetime import datetime

LOG_FILE = "logs/raw_logs.txt"

def collect_logs():
    os.makedirs("logs", exist_ok=True)

    simulated_logs = [
        f"{datetime.now()} - LOGIN - User admin from 192.168.1.5",
        f"{datetime.now()} - LOGIN_FAIL - User guest from 10.0.0.1",
        f"{datetime.now()} - FILE_ACCESS - /etc/passwd by root",
        f"{datetime.now()} - LOGIN_FAIL - User guest from 10.0.0.1"
    ]

    with open(LOG_FILE, "a") as f:
        for log in simulated_logs:
            f.write(log + "\n")

    return simulated_logs
