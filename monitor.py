import time
import os
from parser import parse_logs
from storage import store_logs
from alert import check_alerts

LOG_FILE = "logs/raw_logs.txt"

def monitor_logs():
    print("Real-time log monitoring started...")
    os.makedirs("logs", exist_ok=True)
    
    with open(LOG_FILE, "r") as f:
        # Move to the end of the file
        f.seek(0, os.SEEK_END)

        while True:
            line = f.readline()
            if not line:
                time.sleep(1)
                continue

            log_entry = [line.strip()]
            parsed = parse_logs(log_entry)
            store_logs(parsed)
            check_alerts(parsed)
